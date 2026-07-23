import feedparser

feed_url = "https://www.karmasandhan.com/feed/"

feed = feedparser.parse(feed_url)

print("Total Posts:", len(feed.entries))

for post in feed.entries[:10]:
    print("TITLE :", post.title)
    print("LINK  :", post.link)
    print("-" * 50)
import requests
from bs4 import BeautifulSoup

first_post = feed.entries[0].link

print("\nOpening:", first_post)

response = requests.get(first_post, headers={"User-Agent":"Mozilla/5.0"})

soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("article")
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = f"""
Rewrite this article completely.

Rules:
- 100% unique
- SEO Friendly
- Human written
- Keep facts same
- Create new title
- Create headings
- No plagiarism

Article:
{content.get_text(" ", strip=True)}
"""

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)

print("\n========== AI ARTICLE ==========\n")
print(response.text[:5000])

if content:
    print(content.get_text(" ", strip=True)[:3000])
else:
    print("Content Not Found")
