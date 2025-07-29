# Use an official Python 3.13 image
FROM python:3.13-slim

# Set environment variables
ENV POETRY_VERSION=2.1.3 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=.

# Install Poetry
RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY . /app

# Copy only the necessary files for Poetry to install dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --without dev
