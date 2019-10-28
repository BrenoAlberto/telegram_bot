from pathlib import Path

root_dir = Path('__file__').resolve().parent.parent

def get_path_from_root_dir(path: str) -> str:
    return str(root_dir.joinpath(path))