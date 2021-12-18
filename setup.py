from setuptools import setup, find_packages 

VERSION = '0.0.1'
DESCRIPTION = 'NBA data Scrapper for stats analysis'

# Setting up the package
setup(
    name = "fu-scrapper",
    version = VERSION,
    author = 'Fujyn',
    author_email = "fujyn.contact@gmail.com",
    url = 'https://github.com/Endy02/fu-scrapper',
    description = DESCRIPTION,
    long_description_content_type = 'text/markdown',
    long_description = './README.md',
    packages = find_packages(),
    install_requires = ['pandas','numpy','request','joblib'],
    python_requires = '>=3.7',
    keywords = ['python','sports','data-analysis','csv'],
    classifiers = [
        'Development status :: 1 - Development',
        'Intended Audience :: Python Developers :: Data Scientist',
        'Programming Language :: Python :: 3',  
        'Operating System :: Unix',
        'Operating System :: MacOs :: MacOS X',
        'Operating System :: Windows',
    ]
)