FROM python:3.11-slim

WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Copy your mock API script
COPY src/test/resources/mock_api.py ./mock_api.py

# Expose the port
EXPOSE 9000

# Run the server
CMD ["uvicorn", "mock_api:app", "--host", "0.0.0.0", "--port", "9000"]