from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    """
    Health check endpoint that returns 200 status code.
    """
    return {"status": "ok"}
