import logging
import re
import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_ok(caplog):
    caplog.set_level(logging.INFO)

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "Healthy"
    assert isinstance(data["uptime_seconds"], int)
    assert isinstance(data["system"], dict)
    assert isinstance(data["timestamp"], str)
    assert data["timestamp"].endswith("Z")

    request_id = response.headers.get("X-Request-ID")
    assert request_id is not None and request_id != ""
    # Validate UUID format
    uuid_obj = uuid.UUID(request_id)
    assert str(uuid_obj) == request_id

    # Verify logs were emitted by middleware and health route
    messages = [rec.getMessage() for rec in caplog.records]
    # Middleware start/end
    assert any(m.startswith("start | rid=") and " GET /health " in m for m in messages)
    end_msgs = [m for m in messages if m.startswith("end | rid=") and " GET /health " in m]
    assert end_msgs, "Expected an end log line from request middleware"
    # Health handler logs
    assert any("health_check.success" in m for m in messages)

    # Correlate request ID in logs with response header
    rid_match = re.search(r"rid=([^\s|]+)", end_msgs[-1])
    assert rid_match is not None
    rid_in_log = rid_match.group(1)
    assert rid_in_log == request_id


