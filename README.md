# EE DevOps Workshop API

## Overview
FastAPI application exposing a health endpoint.

## Requirements
- Python 3.10+
- pip

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## URLs
- Health check: [http://localhost:8000/health](http://localhost:8000/health) (also: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health))
- API docs (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- From another device on your LAN: `http://<your-machine-ip>:8000/health`

## Endpoint
- GET `/health` — returns application health and basic system info

### Sample response
```json
{
  "status": "Healthy",
  "timestamp": "2025-05-13T10:30:45Z",
  "system": {
    "python_version": "3.11.8",
    "implementation": "CPython",
    "platform": "macOS-14.5-arm64-arm-64bit",
    "system": "Darwin",
    "release": "23.5.0",
    "machine": "arm64",
    "processor": "Apple M2",
    "hostname": "local",
    "pid": 12345,
    "cwd": "/path/to/project",
    "app_version": "0.1.0"
  },
  "uptime_seconds": 12
}
```

## Logging

- **What is logged**: each HTTP request and response with request ID, client IP, method, path, status code, and latency in ms.
- **Request ID**: returned to clients via `X-Request-ID` header; also available as `request.state.request_id` in handlers.
- **Log level**: controlled by `LOG_LEVEL` env var (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). Defaults to `INFO`.

### Examples

```text
2025-10-26 12:00:00,123 | INFO | ee-devops-workshop | request | start | rid=2b9f... | GET /health | client=127.0.0.1
2025-10-26 12:00:00,125 | INFO | ee-devops-workshop | request | end | rid=2b9f... | GET /health -> 200 | client=127.0.0.1 | latency_ms=2.10
```

### Configure log level

```bash
export LOG_LEVEL=DEBUG
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
