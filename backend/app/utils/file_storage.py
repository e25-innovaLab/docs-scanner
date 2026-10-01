from pathlib import Path
from shutil import copyfileobj

from fastapi import UploadFile


STORAGE_DIR = Path("/app/data")


def get_unique_filename(filename: str) -> str:
    original_path = Path(filename)

    stem = original_path.stem
    suffix = original_path.suffix

    candidate = STORAGE_DIR / filename
    counter = 1

    while candidate.exists():
        candidate = STORAGE_DIR / f"{stem} ({counter}){suffix}"
        counter += 1

    return candidate.name


def save_file(file: UploadFile, filename: str) -> Path:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    unique_filename = get_unique_filename(filename)
    file_path = STORAGE_DIR / unique_filename

    with file_path.open("wb") as destination:
        copyfileobj(file.file, destination)

    return file_path