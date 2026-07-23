import os
import requests


def create_draft(title, content):
    wp_url = os.getenv("WP_URL")
    wp_user = os.getenv("WP_USERNAME")
    wp_pass = os.getenv("WP_APP_PASSWORD")

    data = {
        "title": title,
        "content": content,
        "status": "draft"
    }

    response = requests.post(
        f"{wp_url}/wp-json/wp/v2/posts",
        auth=(wp_user, wp_pass),
        json=data,
        timeout=30
    )

    print("Status Code:", response.status_code)
    print(response.text)

    response.raise_for_status()

    return response.json()
