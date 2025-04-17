# University Chatbot

A specialized chatbot application designed to answer questions about university information using document retrieval and large language models.

## Overview

This project creates an intelligent chatbot that can:
- Process and index university documents (PDFs, etc.)
- Understand natural language questions about university information
- Retrieve relevant information from indexed documents
- Generate accurate, contextual responses using AI language models

## Features

- **Document Processing**: Automatically processes and indexes university documents
- **Semantic Search**: Uses vector embeddings to find the most relevant information
- **Conversational AI**: Leverages OpenAI GPT models for natural language understanding
- **Web Interface**: Simple Flask-based interface for interacting with the chatbot

## Technology Stack

- **Python**: Core programming language
- **LangChain**: Framework for building LLM applications
- **Pinecone**: Vector database for document storage and retrieval
- **OpenAI/Mistral AI**: Language model providers
- **Sentence Transformers**: For generating document embeddings
- **Flask**: Web framework for the user interface

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create and set up environment variables:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file to add your API keys (see API Key Security section below)
4. Add your university documents to the `Data` directory
5. Run the indexing script to process documents:
   ```
   python store_index.py
   ```
6. Start the application:
   ```
   python app.py
   ```

## API Key Security

**⚠️ IMPORTANT: Never commit your actual API keys to Git or GitHub! ⚠️**

This project requires API keys for several services:
- OpenAI API (for GPT models)
- Pinecone (for vector database)
- Mistral AI (optional, for alternative language models)

Follow these best practices:
1. Use the `.env.example` file as a template, which contains placeholders
2. Create your own `.env` file locally with your actual API keys
3. The `.env` file is already in `.gitignore` to prevent accidental commits
4. If you've accidentally committed API keys:
   - Immediately regenerate new API keys on the respective platforms
   - Remove the sensitive file from Git history using:
     ```
     git rm --cached .env
     git commit -m "Remove .env file with API keys"
     ```

## Setting Up API Keys

### OpenAI API
1. Create an account at [OpenAI](https://platform.openai.com/)
2. Generate an API key in your account dashboard
3. Add to your `.env` file: `OPENAI_API_KEY="your_key_here"`

### Pinecone
1. Sign up at [Pinecone](https://www.pinecone.io/)
2. Create an index named "chatbot" with 1536 dimensions (for OpenAI embeddings)
3. Copy your API key and environment from the Pinecone console
4. Add to your `.env` file: `PINECONE_API_KEY="your_key_here"`

### Mistral AI (Optional)
1. Register at [Mistral AI](https://mistral.ai/)
2. Generate an API key 
3. Add to your `.env` file: `MISTRAL_API_KEY="your_key_here"`

## Project Structure

- `app.py`: Main application entry point
- `src/`: Core source code
  - `helper.py`: Utility functions for document processing
  - `prompt.py`: Prompt templates for language models
- `Data/`: Directory for university documents
- `research/`: Experimental notebooks and research
- `store_index.py`: Script for indexing documents in Pinecone

## Usage

1. Start the application
2. Enter questions about university information in the web interface
3. Receive AI-generated responses based on the indexed documents

## License

MIT
