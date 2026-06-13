from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

app = FastAPI(title='FastAPI application for demonstration purposes')

multiply_operations = Counter(
    "multiply_operations_total",
    "Number of multiply operations"
)

Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/actions/multiply")
async def multiply(a: int, b: int):
    multiply_operations.inc()
    return {"result": a * b}
