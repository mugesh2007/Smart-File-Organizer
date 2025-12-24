import logging
import shutil
from pathlib import Path
from .config_loader import load_rules

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(filename=log_dir/"organizer.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def get_category(file_path: Path, rules: dict) -> str:
    suffix = file_path.suffix.lower()
    for category, exts in rules.items():
        if suffix in exts:
            return category
    return "Others"

def safe_move(src: Path, dest_dir: Path) -> bool:
    dest_dir.mkdir(exist_ok=True)
    dest = dest_dir / src.name
    counter = 1
    while dest.exists():
        dest = dest_dir / f"{src.stem}({counter}){src.suffix}"
        counter += 1
    try:
        shutil.move(str(src), str(dest))
        logging.info(f"Moved {src.name} → {dest_dir.name}/")
        return True
    except Exception as e:
        logging.error(f"Failed {src.name}: {e}")
        return False

def organize_folder(root_path: Path, rules: dict) -> int:
    moved = 0
    for item in root_path.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            cat = get_category(item, rules)
            dest = root_path / cat
            if safe_move(item, dest):
                moved += 1
    return moved
