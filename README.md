
# Hisham - Product Inventory Management

A modern product inventory management system built with FastAPI and PostgreSQL, providing a robust RESTful API for tracking and managing product inventory.

## ✨ Features

- **Welcome Endpoint** - `GET /` - Greet message
- **List Products** - `GET /products/` - Retrieve all products
- **Get Product** - `GET /product/{id}` - Fetch a specific product by ID
- **Create Product** - `POST /products/` - Add a new product
- **PostgreSQL Database** - Persistent data storage with SQLAlchemy ORM
- **Docker Support** - Containerized deployment with Docker Compose

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)
```bash
docker-compose up --build
```
This will start both the FastAPI server and PostgreSQL database.

- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Option 2: Local Development

1. **Create and activate virtual environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Linux/Mac
   myenv\Scripts\activate     # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up database:**
   - Ensure PostgreSQL is running on `localhost:5432`
   - Update `DATABASE_URL` in your environment if needed

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Swagger Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📁 Project Structure

```
fastapi-demo/
├── main.py                # FastAPI application with endpoints
├── models.py              # Pydantic request/response models
├── database_model.py      # SQLAlchemy ORM models
├── database.py            # Database configuration & session management
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image configuration
├── compose.yml            # Docker Compose configuration
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 📚 API Usage Examples

### Get Welcome Message
```bash
curl http://localhost:8000/
```

### Get All Products
```bash
curl http://localhost:8000/products/
```

### Get Product by ID
```bash
curl http://localhost:8000/product/1
```

### Create a New Product
```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Monitor",
       "description": "4K monitor",
       "price": 299.99,
       "quantity": 15
     }'
```

## 🏗️ Data Models

### Product Model
```python
{
  "id": integer,           # Unique product identifier
  "name": string,          # Product name
  "description": string,   # Product description
  "price": float,          # Product price
  "quantity": integer      # Available quantity in stock
}
```

## 🗄️ Database

- **Type**: PostgreSQL 15 (Alpine)
- **Connection**: Configured via `DATABASE_URL` environment variable
- **Default Credentials**: 
  - User: `postgres`
  - Password: `12345678`
  - Database: `postgres`
- **Port**: `5432`

## 🛠️ Built With

- [**FastAPI**](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [**Pydantic**](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [**SQLAlchemy**](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [**Uvicorn**](https://www.uvicorn.org/) - ASGI server implementation
- [**PostgreSQL**](https://www.postgresql.org/) - Reliable relational database
- [**Docker**](https://www.docker.com/) - Container platform

## 📝 Environment Variables

When using Docker Compose, the following environment variables are configured:

```
DATABASE_URL=postgresql://postgres:12345678@db:5432/postgres
```

For local development, ensure your PostgreSQL connection string matches this format.