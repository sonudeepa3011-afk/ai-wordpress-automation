from modules.rss import get_latest_posts
from modules.scraper import get_article_content
from modules.ai import rewrite_article
from modules.wordpress import create_draft

RSS_URL = "https://www.karmasandhan.com/feed/"

print("Loading RSS Feed...")

posts = get_latest_posts(RSS_URL, limit=1)

print("Posts Found:", len(posts))

if not posts:
    raise Exception("RSS Feed returned no posts.")

post = posts[0]

print("Title:", post["title"])

print("Fetching Article...")
content = get_article_content(post["link"])

print("Content Length:", len(content))

print("Rewriting with Gemini AI...")
article = rewrite_article(
    post["title"],
    content
)

print("AI Rewrite Completed")

print("Creating WordPress Draft...")

draft = create_draft(
    post["title"],
    article
)

print("====================================")
print("✅ Draft Created Successfully")
print("Draft ID:", draft["id"])
print("Draft Link:", draft["link"])
print("====================================")
