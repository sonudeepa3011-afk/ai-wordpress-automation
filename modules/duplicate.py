import os
import requests

WP_URL = os.getenv("WP_URL")
WP_USER = os.getenv("WP_USERNAME")
WP_PASS = os.getenv("WP_APP_PASSWORD")


def is_duplicate(title):
    url = f"{WP_URL}/wp-json/wp/v2/posts"

    params = {
        "search": title,
        "per_page": 5
    }

    response = requests.get(
        url,
        params=params,
        auth=(WP_USER, WP_PASS)
    )

    if response.status_code != 200:
        print("Duplicate Check Failed")
        return False

    posts = response.json()

    for post in posts:
        if post["title"]["rendered"].strip().lower() == title.strip().lower():
            return True

    return False
