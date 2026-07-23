import os
import re
import requests
from requests.auth import HTTPBasicAuth


WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def is_duplicate(title):

    if not WP_URL:
        print("WP_URL not configured.")
        return False

    endpoint = WP_URL.rstrip("/") + "/wp-json/wp/v2/posts"

    params = {
        "search": title,
        "per_page": 10,
        "status": "any"
    }

    try:

        response = requests.get(
            endpoint,
            params=params,
            auth=HTTPBasicAuth(
                WP_USERNAME,
                WP_APP_PASSWORD
            ),
            timeout=30
        )

        response.raise_for_status()

        posts = response.json()

        target_slug = slugify(title)

        for post in posts:

            post_title = (
                post.get("title", {})
                .get("rendered", "")
                .strip()
                .lower()
            )

            post_slug = post.get("slug", "").strip().lower()

            if post_title == title.strip().lower():
                print("Duplicate Title Found")
                return True

            if post_slug == target_slug:
                print("Duplicate Slug Found")
                return True

        return False

    except Exception as e:

        print("Duplicate Check Error:", e)

        # Duplicate check fail होने पर automation बंद नहीं होगा
        return False
