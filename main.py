from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    print("in root")
    time.sleep(200)
    print("done sleeping")
    return 'done'

@app.on_event("shutdown")
def fun():
    print("In Shutdown")
    time.sleep(100)

