from datetime import datetime, timezone
import logging

from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

from ..utils.system_info import get_system_info, get_uptime_seconds


router = APIRouter()
logger = logging.getLogger("health")


@router.get("/health", summary="Health check", tags=["health"])
def get_health(request: Request):
    rid = getattr(request.state, "request_id", "-")
    logger.info("health_check.start | rid=%s", rid)
    payload = {
        "status": "Healthy",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "system": get_system_info(),
        "uptime_seconds": get_uptime_seconds(),
    }
    logger.info("health_check.success | rid=%s | uptime_seconds=%s", rid, payload["uptime_seconds"])
    return JSONResponse(content=payload, status_code=status.HTTP_200_OK)


