from pathlib import Path
import json

def load_rules(config_path: str = "config/rules.json"):
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config missing: {config_path}")
    with open(config_file) as f:
        return json.load(f)
