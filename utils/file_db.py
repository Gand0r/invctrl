import json
from typing import List
from pathlib import Path

def load_json(path: str) -> List[dict]:
    if Path(path).exists():
        with open(path, "r") as f:
            return json.load(f)
    return []

def save_json(path: str, data: List[dict]):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
