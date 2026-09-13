from src.helper.database import DATA_FILE


def setup_missing_dirs():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}")
        print(f"{DATA_FILE}")


if __name__ == "__main__":
    setup_missing_dirs()
