from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# simple get request
@app.get("/")
def read_root():
    return {"Hello":"World"}


# path parameters
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# query parameters
@app.get("/search")
def search_items(name: str, age: int = 18):
    return {"name": name, "age": age}


#  Request Body (POST Requests)
class User(BaseModel):
    name: str
    age: int
    email: str

class UserResponse(BaseModel):
    id: int = 100
    name: str
    email: str

@app.post("/users", response_model=UserResponse)
def create_user(user: User):
    # return {"message": f"User {user.name} created!", "user_data": user.email}
    return {"id": 100, "name": user.name, "email": user.email}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": f"User {user_id} updated!", "user_data": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted!"}


# Patch request using the Optional Parameter
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int]= None
    email: Optional[str]= "Email not provided"

@app.patch("/users/{user_id}")
def partial_update_user(user_id: int, user: UserUpdate):
    return {"message": f"User {user_id} updated!", "user_data": user}