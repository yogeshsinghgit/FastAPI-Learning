### **Pydantic Models in FastAPI** 🚀  

**Pydantic** is a **data validation** and **serialization** library that FastAPI uses to **validate request data** automatically. It helps ensure that the data sent to an API is **correct, structured, and well-typed** before processing.  

---

## **1️⃣ Why Use Pydantic in FastAPI?**
✅ **Automatic data validation** (checks types like `str`, `int`, `float`).  
✅ **Prevents bad requests** (e.g., missing or incorrect data).  
✅ **Easy to use** (works like Python `dataclass`).  
✅ **Converts JSON data into Python objects**.  

---

## **2️⃣ Defining a Pydantic Model**
🔹 A **Pydantic model** is a class that inherits from `BaseModel`.  
🔹 Each **attribute** is defined with a **type hint** (`str`, `int`, `bool`, etc.).  

### **Example: Defining a User Model**
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```
✔ This model ensures that:  
- `name` is a **string**.  
- `age` is an **integer**.  
- `email` is a **string**.  

---

## **3️⃣ Using Pydantic Model in FastAPI**
🔹 When we receive a **POST request**, FastAPI automatically **validates** the request body using the Pydantic model.

### **Example: Using Pydantic in a FastAPI Route**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the model
class User(BaseModel):
    name: str
    age: int
    email: str

# Create a new user
@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!", "user_data": user}
```
✔ Try **sending a POST request**:  
```json
{
  "name": "Alice",
  "age": 25,
  "email": "alice@example.com"
}
```
✔ FastAPI **validates the request**, ensuring:  
✅ `name` is a string.  
✅ `age` is an integer.  
✅ `email` is a string.  
🚨 **If any field is missing or incorrect**, FastAPI returns a **422 Unprocessable Entity error**.

---

## **4️⃣ Adding Default Values & Optional Fields**
🔹 We can make fields **optional** using `Optional` from `typing`.  
🔹 We can also set **default values**.  

### **Example: Optional Fields & Defaults**
```python
from typing import Optional

class User(BaseModel):
    name: str
    age: int = 18  # Default age is 18
    email: Optional[str] = None  # Email is optional
```
✔ If the user **does not provide an age**, it defaults to `18`.  
✔ If the user **does not provide an email**, it will be `None`.

---

## **5️⃣ Validating Data with Pydantic**
🔹 We can add **custom validations** using Pydantic's built-in types and validators.

### **Example: Custom Validation**
```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=0, lt=120, description="Age must be between 1 and 119")
    email: str
```
✔ `name` must be **between 3 and 50 characters**.  
✔ `age` must be **between 1 and 119**.  
✔ If any rule is violated, FastAPI **automatically returns a 422 error**.

---

## **6️⃣ Returning Pydantic Models (Response Models)**
🔹 We can also **use Pydantic models in responses** to control the output format.

### **Example: Custom Response Model**
```python
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    return {"id": 1, "name": user.name, "email": user.email}
```
✔ The response will **always** follow this structure:  
```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```
