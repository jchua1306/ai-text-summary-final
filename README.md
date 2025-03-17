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

## Example API Request
import requests

url = "http://localhost:8000/summarize/"
payload = {
    "text": "The rapid advancement of artificial intelligence technologies has sparked widespread debate about the future of work, education, and society. As machine learning algorithms become increasingly sophisticated, they are transforming industries ranging from healthcare to transportation, raising both excitement about potential benefits and concerns about disruption. Proponents argue that AI will lead to unprecedented productivity gains, free humans from mundane tasks, and solve complex problems previously thought intractable.",
    "max_length": 100,
    "min_length": 30
}
response = requests.post(url, json=payload)
print(response.json())

## Project Structure
#### app.py: FastAPI application code
#### Dockerfile: Docker configuration
#### docker-compose.yml: Docker Compose configuration
#### requirements.txt: Python dependencies

