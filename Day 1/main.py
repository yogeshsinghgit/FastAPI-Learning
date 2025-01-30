from fastapi import FastAPI
import time, asyncio


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Item Name"}


@app.get("/greet/{user}")
def greet_user(user: str):
    return {"message": f"Hello , {user}"}


@app.get("/sync")
def sync_endpoint():
    time.sleep(5) # blocks the request for 5 seconds
    return {"message": "Synchronous Response"}

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(5) # does not block the request
    return {"message": "Asynchronous Response"}