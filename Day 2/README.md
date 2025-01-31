### **Day 2: FastAPI - Routing & Request Handling** 🚀  

Today, we will cover:  
✅ Defining multiple routes (GET, POST, PUT, DELETE).  
✅ Handling **query parameters**, **path parameters**, and **request bodies**.  
✅ Request validation using **Pydantic models**.  

---

## **1️⃣ Creating Routes in FastAPI**
In FastAPI, we define API routes using **decorators** (`@app.get()`, `@app.post()`, etc.).

### **Basic Route Example**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}
```
✔ **Start the server:** `uvicorn main:app --reload`  
✔ Open **http://127.0.0.1:8000/docs** to see the interactive Swagger UI.

---

## **2️⃣ Path Parameters**
🔹 Path parameters allow us to **capture values from the URL**.  
🔹 Example: `GET /items/42` will capture `42` as `item_id`.

### **Example: Path Parameter**
```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```
✔ Try **`GET /items/10`** → It returns `{ "item_id": 10 }`.

💡 **Data Type Validation:** If you pass a string (`/items/abc`), FastAPI **automatically returns a 422 error** because `item_id` expects an `int`.

---

## **3️⃣ Query Parameters**
🔹 Query parameters are **optional** and appear after `?` in the URL:  
🔹 Example: `/search?name=John&age=25`

### **Example: Query Parameters**
```python
@app.get("/search")
def search_items(name: str, age: int = 18):
    return {"name": name, "age": age}
```
✔ Try `/search?name=John&age=30` → Returns `{ "name": "John", "age": 30 }`.  
✔ Try `/search?name=John` (no age) → Uses **default value** (`age=18`).

---

## **4️⃣ Request Body (POST Requests)**
🔹 When sending data in a request **body**, we use **Pydantic models** for validation.  

### **Example: Sending JSON Data (POST Request)**
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!", "user_data": user}
```
✔ **Test using Swagger UI** (`POST /users/`), send:  
```json
{
  "name": "Alice",
  "age": 25,
  "email": "alice@example.com"
}
```
✔ Returns:  
```json
{
  "message": "User Alice created!",
  "user_data": {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
  }
}
```
💡 **FastAPI automatically validates missing or incorrect data!**  

---

## **5️⃣ PUT (Update) Request Example**
🔹 **Updating existing data** with `PUT` (requires full data).  

### **Example: Updating User**
```python
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": f"User {user_id} updated!", "updated_data": user}
```
✔ Try `PUT /users/1` with JSON:  
```json
{
  "name": "Bob",
  "age": 30,
  "email": "bob@example.com"
}
```
✔ Response:  
```json
{
  "message": "User 1 updated!",
  "updated_data": {
    "name": "Bob",
    "age": 30,
    "email": "bob@example.com"
  }
}
```

---

## **6️⃣ DELETE Request Example**
🔹 `DELETE` requests are used to **remove resources**.

### **Example: Delete a User**
```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted!"}
```
✔ Try `DELETE /users/2`  
✔ Response: `{ "message": "User 2 deleted!" }`

---

## **7️⃣ Handling Optional Parameters**
🔹 We can make parameters **optional** using `Optional` from `typing`.

### **Example: Optional Field**
```python
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

@app.patch("/users/{user_id}")
def partial_update_user(user_id: int, user: UserUpdate):
    return {"message": f"User {user_id} partially updated!", "updated_data": user}
```
✔ Try `PATCH /users/1` with JSON:  
```json
{
  "name": "Charlie"
}
```
✔ Response: `{ "message": "User 1 partially updated!", "updated_data": { "name": "Charlie" } }`

