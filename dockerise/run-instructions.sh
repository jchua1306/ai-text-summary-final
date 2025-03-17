# Save your FastAPI code as app.py

# Build and run using Docker Compose
docker-compose up --build

# Or use Docker directly
docker build -t summarization-api .
docker run -p 8000:8000 summarization-api

# To stop the container if using Docker Compose
docker-compose down

# To stop the container if using Docker directly
docker stop $(docker ps -q --filter ancestor=summarization-api)
