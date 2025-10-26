from datetime import datetime, timezone

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..utils.system_info import get_system_info, get_uptime_seconds


router = APIRouter()


@router.get("/health", summary="Health check", tags=["health"])
def get_health():
    payload = {
        "status": "Healthy",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "system": get_system_info(),
        "uptime_seconds": get_uptime_seconds(),
    }
    return JSONResponse(content=payload, status_code=status.HTTP_200_OK)


