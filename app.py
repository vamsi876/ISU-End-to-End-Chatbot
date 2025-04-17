from flask import Flask, render_template, request, jsonify, session
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


embeddings = download_hugging_face_embeddings()

index_name = 'chatbot'
docsearch = PineconeVectorStore.from_existing_index(embedding=embeddings, index_name=index_name)
retriever = docsearch.as_retriever(search_type="similarity",search_kwargs={"k": 3})

llm = OpenAI(temperature=0.4, max_tokens=500)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    # Initialize chat history if it doesn't exist
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    
    # Initialize chat history if it doesn't exist
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    # Add user message to chat history
    session['chat_history'].append({"role": "user", "content": msg})
    
    responce = rag_chain.invoke({"input": msg})
    print("Responce: ", responce['answer'])
    
    # Add bot response to chat history
    session['chat_history'].append({"role": "bot", "content": responce['answer']})
    
    # Save the updated chat history
    session.modified = True
    
    return str(responce['answer'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
