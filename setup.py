from setuptools import setup, find_packages
setup( name='University chatbot',
      version = '1.0.0',
      author = 'Vamsi Krishna Kollipara',
      author_email = 'kolliparavamsikrishna80@gmail.com',
      packages = find_packages(),
      install_requires = ['sentence-transformers==2.2.2',
                          'langchain',
                          'flask',
                          'pypdf',
                          ])