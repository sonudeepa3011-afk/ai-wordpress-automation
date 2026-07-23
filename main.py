import os
import requests

wp_url = os.getenv("WP_URL")
wp_user = os.getenv("WP_USERNAME")
wp_pass = os.getenv("WP_APP_PASSWORD")

print("WP_URL:", wp_url)
print("WP_USERNAME:", wp_user)
print("WP_PASSWORD Found:", "Yes" if wp_pass else "No")

if not wp_url or not wp_user or not wp_pass:
    raise Exception("One or more GitHub Secrets are missing.")

url = f"{wp_url}/wp-json/wp/v2/users/me"

response = requests.get(url, auth=(wp_user, wp_pass), timeout=30)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("✅ WordPress Connected Successfully")
    print("User:", response.json().get("name"))
else:
    print("❌ Connection Failed")
    print(response.text)

if content:
    print(content.get_text(" ", strip=True)[:3000])
else:
    print("Content Not Found")
