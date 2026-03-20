from fastapi import FastAPI

app = FastAPI(title="DevOps Simple Demo")


@app.get("/")
def root() -> dict:
    return {"message": "Hello from the DevOps demo!"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

