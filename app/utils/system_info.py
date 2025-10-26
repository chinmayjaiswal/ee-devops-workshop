import os
import platform
import socket
import time
from typing import Any, Dict


_PROCESS_START_TIME = time.time()


def get_uptime_seconds() -> int:
    """Return the process uptime in whole seconds."""
    return int(time.time() - _PROCESS_START_TIME)


def get_system_info() -> Dict[str, Any]:
    """Collect lightweight, dependency-free system information."""
    return {
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
        "cwd": os.getcwd(),
        "app_version": os.getenv("APP_VERSION", "0.1.0"),
    }


