# Import necessary libraries for document processing and embeddings
from langchain.document_loaders import PyPDFLoader, DirectoryLoader  # For loading PDF documents
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting documents into chunks
from langchain.embeddings import HuggingFaceEmbeddings  # For creating text embeddings

def load_documents(data):
    """
    Load PDF documents from a specified directory.
    
    Args:
        data (str): Path to the directory containing PDF files
        
    Returns:
        list: List of loaded document objects
    """
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# Example usage: extracted_data = load_documents("Data")
def text_splitter(extracted_data):
    """
    Split documents into smaller chunks for better processing.
    
    Args:
        extracted_data (list): List of document objects to split
        
    Returns:
        list: List of text chunks with 500 characters each and 20 character overlap
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chuncks=text_splitter.split_documents(extracted_data)
    return text_chuncks
# Example usage: text_chuncks=text_splitter(extracted_data)
# Example debug: print("Length of text chunks: ", len(text_chuncks))

def download_hugging_face_embeddings():
    """
    Initialize the Hugging Face embedding model.
    
    Returns:
        HuggingFaceEmbeddings: Initialized embedding model that converts text to vectors
                              using the all-MiniLM-L6-v2 model (384 dimensions)
    """
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings
# Example usage: embeddings=download_hugging_face_embeddings()