from fastapi import FastAPI
from .logging_config import configure_logging
from .middleware.request_logging import RequestLoggingMiddleware

from .routers.health import router as health_router


configure_logging(app_name="ee-devops-workshop")

app = FastAPI(title="EE DevOps Workshop API")


app.include_router(health_router, prefix="")

# Register middlewares
app.add_middleware(RequestLoggingMiddleware)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


