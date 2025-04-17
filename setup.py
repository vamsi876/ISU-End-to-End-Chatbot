from setuptools import setup, find_packages

# Setup configuration for the University chatbot package
setup( name='University chatbot',      # Name of the package
      version = '1.0.0',               # Version number of the package
      author = 'Vamsi Krishna Kollipara',  # Author's name
      author_email = 'kolliparavamsikrishna80@gmail.com',  # Author's email
      packages = find_packages(),      # Automatically find and include all packages
      install_requires = [             # List of dependencies required by the package
                          'sentence-transformers==2.2.2',  # For text embeddings
                          'langchain',                     # For document processing
                          'flask',                         # For web application
                          'pypdf',                         # For PDF handling
                          ])