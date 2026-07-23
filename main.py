import os
import requests

wp_url = os.getenv("WP_URL")
wp_user = os.getenv("WP_USERNAME")
wp_pass = os.getenv("WP_APP_PASSWORD")

post = {
    "title": "AI Automation Test Post",
    "content": """
<h2>This is a Test Draft</h2>

<p>This draft has been created automatically from GitHub Actions.</p>

<p>If you can see this in WordPress, the connection is working perfectly.</p>
""",
    "status": "draft"
}

response = requests.post(
    f"{wp_url}/wp-json/wp/v2/posts",
    auth=(wp_user, wp_pass),
    json=post
)

print("Status:", response.status_code)
print(response.text)
