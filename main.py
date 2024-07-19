from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    print("in root")
    time.sleep(10000)
    return 'done'

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.on_event("shutdown")
def fun():
    print("In Shutdown")
    time.sleep(10000)