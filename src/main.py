from fastapi import FastAPI

app = FastAPI(title='FastAPI application for demonstration purposes')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/actions/multiply")
async def multiply(a: int, b: int):
    return {"result": a * b}
