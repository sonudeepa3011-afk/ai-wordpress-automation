import os
import re
import requests
from requests.auth import HTTPBasicAuth


WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

POST_STATUS = os.getenv("POST_STATUS", "draft")
DEFAULT_CATEGORY = int(os.getenv("DEFAULT_CATEGORY", "1"))


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def create_draft(title, content):

    if not WP_URL:
        raise Exception("WP_URL missing")

    endpoint = WP_URL.rstrip("/") + "/wp-json/wp/v2/posts"

    excerpt = content[:250]

    data = {
        "title": title,
        "content": content,
        "status": POST_STATUS,
        "slug": slugify(title),
        "excerpt": excerpt,
        "categories": [DEFAULT_CATEGORY],
    }

    response = requests.post(
        endpoint,
        json=data,
        auth=HTTPBasicAuth(
            WP_USERNAME,
            WP_APP_PASSWORD
        ),
        timeout=60
    )

    if response.status_code not in (200, 201):
        print(response.text)
        raise Exception(
            f"WordPress Error {response.status_code}"
        )

    return response.json()
