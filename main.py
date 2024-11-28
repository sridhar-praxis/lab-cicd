from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Update. Hello, CI/CD with FastAPI!"}
