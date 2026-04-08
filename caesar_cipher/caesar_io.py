from pathlib import Path


def read_text_file(path: str) -> str:
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p}")

    if not p.is_file():
        raise ValueError(f"Not a valid file: {p}")

    return p.read_text(encoding="utf-8", errors="ignore")


def write_text_file(path: str, content: str) -> None:
    p = Path(path)

    # Create parent directories if missing
    p.parent.mkdir(parents=True, exist_ok=True)

    p.write_text(content, encoding="utf-8")