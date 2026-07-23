import requests
from bs4 import BeautifulSoup

url = "https://karmasandhan.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

count = 0

for link in links:
    title = link.get_text(strip=True)
    href = link.get("href")

    if title and href and href.startswith("http"):
        print(title)
        print(href)
        print("-------------------------")
        count += 1

    if count == 10:
        break
