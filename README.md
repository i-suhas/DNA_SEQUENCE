# DNA_SEQUENCE
DNA Sequence Encryption and Decryption

                 project_folder/
                      │
                      ├── app.py
                      └── templates/
                           └── index.html

    #This GitHub repository contains a DNA sequence encryption and decryption tool implemented in Python using Flask. 
    The tool provides a simple web interface for encrypting and decrypting DNA sequences using a substitution cipher. 
    Users can input a DNA sequence and a 4-character encryption key, and the tool will perform encryption and decryption operations, 
    displaying the results on the webpage. The project is implemented following best practices for web development and includes documentation for ease of use.

The implementation utilizes Python and the Flask web framework. Key components of the implementation include:

app.py: This Python script contains the Flask application. It defines routes for handling HTTP requests, including rendering the HTML template for the homepage and processing form submissions.
index.html: This HTML template provides the web interface for the tool. It includes a form for inputting the DNA sequence and encryption key, as well as sections for displaying the encrypted and decrypted sequences.
encryption.py: This module contains functions for creating a substitution map for encryption, encrypting and decrypting DNA sequences, and validating DNA sequences.
requirements.txt: This file lists the Python dependencies required by the project, including Flask.
templates/ directory: This directory contains HTML templates used by the Flask application. In this case, it only includes the index.html template.
static/ directory: This directory can be used to store static files such as CSS stylesheets or JavaScript files. In this project, it is not used.
To use the project, users can clone the GitHub repository and run the Flask application locally. They can then access the web interface in their browser to encrypt and decrypt DNA sequences.
