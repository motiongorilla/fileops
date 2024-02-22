from pathlib import Path
import zipfile

root = Path("./")
paths = root.glob("**/[!.]*")

for p in paths:
    if not p.parts[0].startswith(".") and p.is_dir():
        zip_path = p / Path("archive.zip")
        files = p.rglob("*.txt")
        with zipfile.ZipFile(zip_path, "w") as zf:
            for f in files:
                zf.write(f)




