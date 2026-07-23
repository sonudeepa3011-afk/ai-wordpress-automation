import os
import requests

wp_url = os.getenv("WP_URL")
wp_user = os.getenv("WP_USERNAME")
wp_pass = os.getenv("WP_APP_PASSWORD")

url = f"{wp_url}/wp-json/wp/v2/users/me"

response = requests.get(url, auth=(wp_user, wp_pass))

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("✅ WordPress Connected Successfully")
    print(response.json()["name"])
else:
    print("❌ Connection Failed")
    print(response.text)

if content:
    print(content.get_text(" ", strip=True)[:3000])
else:
    print("Content Not Found")
