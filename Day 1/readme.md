

## What is FastAPI?
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3

It is based on:
* Type hints
* Asychronous Support
* Speed
* Automatic Docs

## Step 1: Create Virtual Env

```
python -m venv fastapi_env
source fastapi_env/bin/activate  # On macOS/Linux
fastapi_env\Scripts\activate  # On Windows
```

## Step 2: Install FastAPI & Uvicorn
```
pip install fastapi uvicorn
```

- fastapi → The framework itself.
- uvicorn → ASGI server to run FastAPI apps.

### Step 3: Create main.py file and code for FastAPI app/routes.

...


## Step 4:  Running the FastAPI App

```
uvicorn main:app --reload
```
- main → The file containing the FastAPI app.
main:app → main.py file and app instance.
--reload → Enables auto-reloading (useful for development).

## Step 5: Test the code:

Open your browser and visit:

🔹 http://127.0.0.1:8000 → Shows { "message": "Hello, FastAPI!" }

🔹 http://127.0.0.1:8000/items/10 → Shows { "item_id": 10, "description": "This is an item"}

FastAPI provides auto-generated API docs:

🔹Swagger UI → http://127.0.0.1:8000/docs

🔹ReDoc → http://127.0.0.1:8000/redoc