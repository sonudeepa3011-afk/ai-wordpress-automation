import requests
from bs4 import BeautifulSoup


def get_article_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find("article")

    if article:
        return article.get_text("\n", strip=True)

    return ""
