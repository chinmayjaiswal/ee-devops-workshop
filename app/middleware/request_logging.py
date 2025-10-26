import logging
import time
import uuid
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware that logs incoming requests and responses with latency and a request ID."""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
        self.logger = logging.getLogger("request")

    async def dispatch(self, request: Request, call_next: Callable):
        request_id = str(uuid.uuid4())
        start_time = time.perf_counter()

        # Attach request ID to state so handlers can reuse it if desired
        request.state.request_id = request_id

        client_host = request.client.host if request.client else "-"
        method = request.method
        path = request.url.path

        self.logger.info(
            "start | rid=%s | %s %s | client=%s",
            request_id,
            method,
            path,
            client_host,
        )

        try:
            response = await call_next(request)
        except Exception as exc:  # Let exception be handled upstream after logging
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            self.logger.exception(
                "error | rid=%s | %s %s | client=%s | latency_ms=%.2f",
                request_id,
                method,
                path,
                client_host,
                elapsed_ms,
            )
            raise exc

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0

        # Propagate request ID back to client
        response.headers["X-Request-ID"] = request_id

        self.logger.info(
            "end | rid=%s | %s %s -> %s | client=%s | latency_ms=%.2f",
            request_id,
            method,
            path,
            response.status_code,
            client_host,
            elapsed_ms,
        )

        return response


