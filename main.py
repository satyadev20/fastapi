from fastapi import FastAPI, Request
import time

app = FastAPI()

c=0

@app.get("/")
def read_root():
    print("in root ")
    time.sleep(200)
    print("done sleeping")
    return 'done'

@app.on_event("shutdown")
def fun():
    global c
    print("In Shutdown")
    while c!=0:
        print("sleeping")
        time.sleep(10)
    print("Shutdowning Down")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    global c
    c=c+1
    response = await call_next(request)
    c=c-1
    return response