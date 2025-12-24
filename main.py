from pathlib import Path
import argparse
import sys
from organizer.config_loader import load_rules  
from organizer.core import organize_folder     

def get_user_folder():
    while True:
        folder = input("Enter folder path to organize (or Enter for current folder): ").strip()
        if not folder:
            return Path(".").resolve()
        path = Path(folder).expanduser().resolve()
        if not path.exists():
            print(f" Folder not found: {path}")
            continue
        if not path.is_dir():
            print(f"Not a folder: {path}")
            continue
        return path 
def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer for PC")
    parser.add_argument('target', nargs='?', default='.', help="Folder to organize (default: .)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would move")
    args = parser.parse_args()
    
    # Interactive OR CLI argument
    root = get_user_folder() 
    # root = Path(args.target).resolve() if args.target else get_user_folder()
    
    print(f"Organizing: {root}")
    print(f"Files found: {sum(1 for f in root.iterdir() if f.is_file())}")
    
    rules = load_rules()
    print(f"Categories: {list(rules.keys())}")

    if args.dry_run:
        print("Dry run - no files moved")
        for item in root.iterdir():
            if item.is_file():
                print(f"  → {item.name} → Others/")
        return
    
    input("Press Enter to start organizing...")
    moved = organize_folder(root, rules) 
    print(f"Moved {moved} files! Check logs/organizer.log")

if __name__ == "__main__":
    main()