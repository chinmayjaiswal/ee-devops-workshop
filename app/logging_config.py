import logging
import os
from typing import Optional


def _get_log_level_from_env(default_level: int = logging.INFO) -> int:
    level_name = os.getenv("LOG_LEVEL", "").upper().strip()
    if not level_name:
        return default_level
    mapping = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "NOTSET": logging.NOTSET,
    }
    return mapping.get(level_name, default_level)


def configure_logging(app_name: Optional[str] = None) -> None:
    """Configure application-wide logging.

    Idempotent: safe to call multiple times.
    Honors LOG_LEVEL env var.
    """
    root_logger = logging.getLogger()

    # Avoid duplicating handlers if configure_logging is called more than once
    if getattr(root_logger, "_app_logging_configured", False):
        return

    log_level = _get_log_level_from_env()
    root_logger.setLevel(log_level)

    formatter_parts = [
        "%(asctime)s",
        "%(levelname)s",
        f"{app_name}" if app_name else "app",
        "%(name)s",
        "%(message)s",
    ]
    formatter = logging.Formatter(" | ".join(formatter_parts))

    # Stream handler to stdout (uvicorn also writes to stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(stream_handler)

    # Mark as configured
    setattr(root_logger, "_app_logging_configured", True)


