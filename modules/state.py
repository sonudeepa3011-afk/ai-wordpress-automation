import json
import os

FILE = "data/processed.json"


def load_processed():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_processed(data):

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
