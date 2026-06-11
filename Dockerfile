FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Default to compose service DB so image works when run with docker-compose
ENV DATABASE_URL=postgresql://postgres:12345678@localhost:5432/postgres

# Copy requirements first for better cache behavior
COPY requirements.txt .

# Install build dependencies and install Python requirements
RUN pip3 install -r requirements.txt

# Copy application files
COPY ./database_model.py ./database.py ./main.py ./models.py ./requirements.txt ./

# Start the uvicorn app on all interfaces and use port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]