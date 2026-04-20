from fastapi import FastAPI
from fastapi.requests import Request
import uvicorn

app = FastAPI()

@app.get("/")
async def get_root(request: Request) -> None:
    return "Hello from Effective Mobile!"

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host='127.0.0.1',
        port=8080,
        reload=True
    )