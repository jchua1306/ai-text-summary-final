# ai-text-summary-final

Step-by-Step Instructions

Create the project structure:

Create a new directory for your project
Save your FastAPI code as app.py
Create the Dockerfile and requirements.txt with the content I provided
Optionally, create docker-compose.yml if you want to use Docker Compose


Build and run the Docker container:
With Docker Compose (recommended):
bashCopydocker-compose up --build
Or with plain Docker:
bashCopydocker build -t summarization-api .
docker run -p 8000:8000 summarization-api

Access your API:

The API will be available at http://localhost:8000
API documentation will be at http://localhost:8000/docs
