from modules.rss import get_latest_posts
from modules.scraper import get_article_content
from modules.ai import rewrite_article
from modules.wordpress import create_draft
from modules.duplicate import is_duplicate

RSS_URL = "https://www.karmasandhan.com/feed/"

posts = get_latest_posts(RSS_URL, limit=5)

print("Posts Found:", len(posts))

for post in posts:

    print("=" * 50)
    print("Title:", post["title"])

    # Duplicate Check
    if is_duplicate(post["title"]):
        print("⏭ Duplicate Found - Skipping")
        continue

    print("✅ New Post")

    print("Fetching Article...")
    content = get_article_content(post["link"])

    print("Content Length:", len(content))

    print("Rewriting with Gemini...")
    article = rewrite_article(
        post["title"],
        content
    )

    print("Creating Draft...")

    draft = create_draft(
        post["title"],
        article
    )

    print("✅ Draft Created:", draft["id"])
