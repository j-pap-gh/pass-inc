# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Copy pyproject and poetry.lock (if present) and install dependencies
COPY pyproject.toml* poetry.lock* /app/
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI app with uvicorn (use gunicorn+uvicorn workers in production if preferred)
CMD ["uvicorn", "src.pass_inc.main:app", "--host", "0.0.0.0", "--port", "8000"]
