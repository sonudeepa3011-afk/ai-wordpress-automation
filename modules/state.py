import json
import os


FILE = "data/processed.json"


def ensure_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_processed():

    ensure_file()

    try:

        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                return data

            return []

    except Exception:

        return []


def save_processed(data):

    ensure_file()

    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def already_processed(link):

    processed = load_processed()

    return link in processed


def mark_processed(link):

    processed = load_processed()

    if link not in processed:

        processed.append(link)

        save_processed(processed)

        print("Saved:", link)
