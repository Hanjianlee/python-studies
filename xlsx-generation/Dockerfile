# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the Poetry project files (pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the entire project into the container
COPY . /app/

# Expose any necessary ports
# EXPOSE 8000

# Define the command to run your script
CMD ["python", "main.py"]
