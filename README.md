# Products Management 🚀

## Description ℹ️

This project is an API for managing inventory and products. It is implemented using FastAPI and SQLAlchemy.

## Installation 💻

1. First, clone the repository:

```
git clone https://github.com/kostomeister/fastapi-product-management
```

2. Navigate to the project directory:

```
cd fastapi-product-management
```

3. Create and activate a virtual environment:

   - For Windows 🖥️:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   - For Linux 🐧:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Run database migrations:

```
alembic upgrade head
```

6. Run the program:

```
uvicorn main:app --reload
```

After that, the program will be available at http://127.0.0.1:8000.

## Usage 📝

The API has two main parts: managing inventory and products. You can access the following endpoints:

- `/api/v1/inventory`: endpoints for managing inventory.
- `/api/v1/products`: endpoints for managing products.

Check the API documentation available at http://127.0.0.1:8000/docs for more detailed information on how to use each endpoint.

