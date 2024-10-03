# ERP Chatbot Project

## Overview

The **ERP Chatbot Project** is an innovative solution designed to streamline document processing, text extraction, entity recognition, summarization, and document classification for ERP systems. It provides a user-friendly interface using **Streamlit** for the frontend and a robust backend powered by **Flask** and state-of-the-art machine learning models. The solution is scalable and capable of handling different file formats like PDFs, images, and Word documents, allowing users to easily extract and process data, store it in MongoDB, and classify documents using pretrained models from Hugging Face.

## Project Structure

```
erp_chatbot_project/
 |-------uploads                  # Directory for uploaded documents
├── backend/                     
│   ├── app.py                   # Main Flask application
│   ├── nlp_service.py           # NLP functions (e.g., NER)
│   ├── ocr_service.py           # Document extraction service using Tesseract OCR
│   ├── requirements.txt         # Python dependencies for the backend
│   ├── utils.py                 # Utility functions for document processing
│
├── frontend/                    
│   ├── app.py                   # Main Streamlit application
│   ├── requirements.txt         # Python dependencies for the frontend
│   ├── auth.py                  # User authentication handling
│   ├── home.py                  # Home page for the application
│   └── usermanagement.py        # User management features
│
├── models/                      
│   ├── document_classifier.py   # Document classification model
│   └── ner_model.py             # NER model for entity extraction
│
├── tests/                       
│   ├── test_app.py              # Tests for Flask app
│   └── test_nlp.py              # Tests for NLP functions
│   └── test_auth.py             # Tests for authentication and user management

```
## ER Diagram
![8w4wJ3xo](https://github.com/user-attachments/assets/b0a1a540-5e25-4b73-ae3b-aef91e7f5570)


## Software Architecture

The ERP Chatbot Project is designed using a modular architecture that separates concerns between different components. The main components of the architecture are as follows:

1. **Frontend**: Built with **Streamlit**, the frontend handles user interactions, displays documents, and provides an interface for uploading files and viewing results. It communicates with the backend via API calls.

2. **Backend**: The backend, powered by **Flask**, manages the core functionalities of the application:
   - **Document Upload and Processing**: Receives uploaded documents, processes them using OCR, and performs NLP tasks.
   - **NLP Services**: Includes modules for text extraction (using Tesseract OCR), entity recognition (NER), and document classification.
   - **Database Integration**: Manages interactions with **MongoDB** to store user data and processed documents.

3. **Machine Learning Models**: The project utilizes pretrained models from Hugging Face for tasks like summarization and document classification, allowing for efficient processing of text data.

4. **Utilities**: A collection of utility functions that support various functionalities, such as file handling and data processing.

The architecture supports scalability, allowing additional features and models to be integrated easily. This modular approach also facilitates testing and maintenance.

## Key Features

1. **Text Extraction**: Extracts text from images and documents using Tesseract OCR.
2. **Summarization**: Summarizes long documents into concise paragraphs using Hugging Face's summarization model.
3. **Entity Extraction**: Extracts key entities (names, dates, locations, etc.) from documents.
4. **Document Classification**: Uses Hugging Face’s text classification pipeline to categorize documents into predefined classes.
5. **User Authentication**: User management and authentication features for secured access.
6. **MongoDB Integration**: Stores uploaded documents and user data in MongoDB.
7. **File Conversion**: Converts extracted text to PDF and Word formats for easy download.

## Why Our Solution is Unique

1. **End-to-End Document Management**: Unlike many solutions that only focus on a single aspect of document processing, our project handles everything from text extraction to entity recognition, summarization, classification, and file conversion—all in one platform.
   
2. **Integration with Modern ML Models**: By integrating state-of-the-art machine learning models from Hugging Face, our solution can handle complex NLP tasks like summarization and classification with high accuracy.

3. **Streamlined User Experience**: With a simple, intuitive frontend built using Streamlit, users with minimal technical expertise can manage document workflows without hassle.

4. **Scalability**: This project is built with scalability in mind. Whether you’re working with small sets of documents or need to scale up for enterprise use cases, the solution can be easily extended.

5. **Security and User Management**: Secure authentication and user role management ensure that sensitive documents and operations are protected and can only be accessed by authorized users.

## Team Contributions

The contributions of each team member to the ERP Chatbot Project are as follows:

### [Md Qamar Hussain](https://github.com/mdqamarhussain)  (Team Leader) 
- Led the overall project management and coordination between team members.
- Designed and implemented the backend Flask application.
- Developed the NLP service for entity recognition.
- Managed database integration with MongoDB.

### [Faizan Talib Khan](https://github.com/FAIZANTKHAN)
- Developed the frontend using Streamlit, focusing on user interface design.
- Implemented user authentication and management features.
- Created the home page and ensured seamless navigation in the application.
- Conducted testing and debugging of the frontend functionalities.

### [Vikram Rajak](https://github.com/Vikram334)
- Implemented the OCR service using Tesseract for text extraction.
- Developed the document classification model using Hugging Face.
- Worked on utility functions for document processing and handling file uploads.
- Contributed to the testing of the document processing features.

### [Gagandeep Singh](https://github.com/Gagandeepsn)
- Assisted in the development of the backend application.
- Implemented the summarization feature using Hugging Face's models.
- Worked on integrating the NLP services with the frontend.
- Conducted performance testing and optimization for the application.

## Installation

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Tesseract Installation

Tesseract is required for the OCR functionality. Follow the instructions below based on your operating system:

#### Windows

1. Download the Tesseract installer from the official GitHub repository: [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the installer and follow the setup instructions.
3. Add Tesseract to your system PATH:
   - Right-click on `This PC` or `My Computer` and select `Properties`.
   - Click on `Advanced system settings` and then `Environment Variables`.
   - Find the `Path` variable in the "System variables" section and click `Edit`.
   - Add the path to the Tesseract installation (e.g., `C:\Program Files\Tesseract-OCR`).
4. Verify the installation by running `tesseract -v` in the command prompt.

#### Linux

1. Open your terminal.
2. Install Tesseract using the package manager:
   ```bash
   sudo apt-get install tesseract-ocr
   ```
3. Verify the installation by running `tesseract -v` in the terminal.

#### macOS

1. Open your terminal.
2. Install Tesseract using Homebrew:
   ```bash
   brew install tesseract
   ```
3. Verify the installation by running `tesseract -v` in the terminal.

## Usage

To run the **ERP Chatbot Project**, follow these instructions:

### Step 1: Run the Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
  
2. Start the Flask backend server:
   ```bash
   python app.py
   ```
   The Flask server will start running on `http://127.0.0.1:5000` or another specified port.

### Step 2: Run the Frontend

1. Open a new terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Start the Streamlit frontend:
   ```bash
   streamlit run app.py
   ```

   This will launch the frontend interface, accessible via the URL provided by Streamlit (usually `http://localhost:8501`).

### Step 3: Use the Application

1. Open the Streamlit URL in your browser.
2. Log in or sign up to access the system.
3. Upload a document (image, PDF, or Word file) to extract text.
4. Use the provided options to perform tasks like text extraction, entity recognition, summarization, and document classification.
5. Download the processed results as a PDF or Word document directly from the interface.
