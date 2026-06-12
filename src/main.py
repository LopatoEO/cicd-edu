from fastapi import FastAPI

app = FastAPI(title='FastAPI application for demonstration purposes fhdskfjbsdjkfbjksdbfjsbdjfbdjsbfljsbdfjbsdjkfbjksdbfjbdsfjbdjlbfkjsbdflbsdkbfjlbfjbsdfljbsdkfb jdsbfosdbfmdsbfjsbdfosdhbf')

@app.get("/")
async def root():
    return {"message": "Hello World"}