from fastapi import FastAPI

app = FastAPI()


@app.get("/health", status_code=200)
def health_check():
    """
    Health check endpoint that returns 200 status code.
    """
    return {"status": "ok"}
