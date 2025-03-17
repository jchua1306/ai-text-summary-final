# ai-text-summary-final

## AI Text Summarization API
A FastAPI application that provides an API for text summarization using the BART Large CNN model from Facebook/Meta AI.

## Features

RESTful API endpoint for text summarization
Based on the facebook/bart-large-cnn pre-trained model
Customizable summary parameters (length, sampling)
Containerized with Docker for easy deployment
Auto-generated API documentation with Swagger UI

## Requirements

Python 3.9+
Docker Desktop (for containerized deployment)
Git (for version control)

## Installation
### Option 1: Using Docker (Recommended)

1. Clone the repository:

bashCopygit clone https://github.com/jchua1306/ai-text-summary-final.git
cd ai-text-summary-final

2. Build and start the Docker container:

bashCopydocker-compose up --build

### Option 2: Local Installation

1. Clone the repository:

bashCopygit clone https://github.com/jchua1306/ai-text-summary-final.git
cd ai-text-summary-final

2. Create and activate a virtual environment:

bashCopypython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

bashCopypip install -r requirements.txt

4. Run the application:

bashCopyuvicorn app:app --reload

## Usage
Once the application is running, you can access:

API endpoint: http://localhost:8000/summarize/
API documentation: http://localhost:8000/docs


## Project Structure
#### app.py: FastAPI application code
#### Dockerfile: Docker configuration
#### docker-compose.yml: Docker Compose configuration
#### requirements.txt: Python dependencies

