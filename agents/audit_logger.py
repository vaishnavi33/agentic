import json
from datetime import datetime
import os


LOG_FILE = "logs/audit_log.jsonl"


def safe_serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    try:
        return str(obj)
    except Exception:
        return "UNSERIALIZABLE_OBJECT"


def log_decision(entry: dict):

    os.makedirs("logs", exist_ok=True)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        **entry
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry, default=safe_serialize) + "\n")