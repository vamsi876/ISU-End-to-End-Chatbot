# This script creates the project structure for the University chatbot
# It creates the necessary files and directories for the project

import os
from pathlib import Path
import logging

# Configure logging to display timestamp and message
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")

# List of files to be created for the project structure
list_of_files = [
    ".env",                     # Environment variables file
    "src/__init__.py",          # Python package indicator for src directory
    "src/helper.py",            # Helper functions for the application
    "src/prompt.py",            # Prompt templates for language models
    "setup.py",                 # Package installation configuration
    "app.py",                   # Main application entry point
    "research/trails.ipynb"     # Jupyter notebook for research and experimentation
]
for filepath in list_of_files:
    filepath = Path(filepath)   # Convert string path to Path object
    filedir, filename = os.path.split(filepath)  # Split path into directory and filename
    if filedir != "":
        # Create directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create empty file if it doesn't exist or is empty
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        # Log if file already exists
        logging.info(f"File already exists: {filepath}")
