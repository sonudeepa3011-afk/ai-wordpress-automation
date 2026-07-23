import requests
from bs4 import BeautifulSoup

url = "https://www.karmasandhan.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("article")

print("Total Articles:", len(articles))

for article in articles[:10]:
    a = article.find("a", href=True)

    if a:
        print("TITLE:", a.get_text(strip=True))
        print("LINK :", a["href"])
        print("-" * 50)
