from fastapi import FastAPI

from .routers.health import router as health_router


app = FastAPI(title="EE DevOps Workshop API")


app.include_router(health_router, prefix="")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


