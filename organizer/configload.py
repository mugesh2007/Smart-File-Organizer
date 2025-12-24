from pathlib import Path 
from typing import Dict, List
import json

def load_rule(config_path: str = "config/rules.json") ->Dict[str, List[str]]:
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    with open(config_path) as f:
        return json.load(f)
    