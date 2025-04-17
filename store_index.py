
# This script is used to store the document chunks in the Pinecone vector database
#if you have already created the index, you can skip the creation part

from src.helper import load_documents, text_splitter, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
# from google.protobuf import runtime_version

# Load environment variables from .env file
load_dotenv()

# Get Pinecone API key from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Load PDF documents from the Data directory
extracted_data = load_documents("Data")
# Split the documents into smaller chunks for better processing
text_chuncks=text_splitter(extracted_data)
# Initialize the embedding model to convert text to vectors
embeddings=download_hugging_face_embeddings()

# Initialize Pinecone client with our API key
pc=Pinecone(api_key=PINECONE_API_KEY)
# Name of our vector index in Pinecone
index_name = 'chatbot'

# Create a new Pinecone index with appropriate settings
# Using 384 dimensions to match our embedding model output size
pc.create_index( name=index_name, dimension=384,
                metric='cosine', spec=ServerlessSpec(cloud='aws', region='us-east-1')
                )
# Store our document chunks in the Pinecone vector database
# This allows for semantic search of our documents
docsearch = PineconeVectorStore.from_documents(
    documents=text_chuncks,
    embedding=embeddings,
    index_name=index_name,
    )

print("Pinecone database created and data successfully sent!")
