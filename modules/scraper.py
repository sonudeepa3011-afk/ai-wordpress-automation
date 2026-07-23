import requests
import time
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}


ARTICLE_SELECTORS = [
    "article",
    ".entry-content",
    ".post-content",
    ".td-post-content",
    ".single-content",
    ".content",
    ".post-body",
    ".article-content",
    ".story-content",
    ".main-content",
    "#content",
    ".entry",
]


def clean_text(text):

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if line:
            lines.append(line)

    return "\n\n".join(lines)


def get_article_content(url):

    print(f"Scraping: {url}")

    for attempt in range(1, 4):

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=30
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove unwanted tags
            for tag in soup(["script", "style", "noscript", "iframe"]):
                tag.decompose()

            article = None

            for selector in ARTICLE_SELECTORS:

                article = soup.select_one(selector)

                if article:
                    break

            if article is None:
                article = soup.body

            if article is None:
                print("❌ Article Not Found")
                return ""

            text = article.get_text("\n", strip=True)

            text = clean_text(text)

            if len(text) < 300:
                print("⚠ Very Small Article")

            print(f"✅ Content Length: {len(text)}")

            return text

        except Exception as e:

            print(f"Attempt {attempt}/3 Failed")
            print(e)

            if attempt < 3:
                time.sleep(2)

    print("❌ Failed To Scrape")

    return ""
