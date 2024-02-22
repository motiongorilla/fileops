from pathlib import Path

root = Path("./")
paths = root.iterdir()

for p in paths:
    if p.is_dir():
        dir_name = p.name
        if not dir_name.startswith("."):
            inside_files = p.iterdir()
            for f in inside_files:
                new_name = dir_name + f.stem + f.suffix
                new_path = f.with_name(new_name)
                f.rename(new_path)
