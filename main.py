from fastapi import FastAPI




app = FastAPI(''
''FastAPI application for demonstration purposes''')

@app.get("/")
async def root():
    return {"message": "Hello World"}