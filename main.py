from modules.rss import get_latest_posts
from modules.scraper import get_article_content
from modules.ai import rewrite_article
from modules.wordpress import create_draft
from modules.duplicate import is_duplicate
from modules.state import already_processed, mark_processed

RSS_URL = "https://www.karmasandhan.com/feed/"

posts = get_latest_posts(RSS_URL, limit=1)

print("Posts Found:", len(posts))

for post in posts:

    print("=" * 60)
    print("Title:", post["title"])

    # Check processed.json
    if already_processed(post["link"]):
        print("⏭ Already Processed (State File)")
        continue

    # Check WordPress
    if is_duplicate(post["title"]):
        print("⏭ Duplicate in WordPress")
        mark_processed(post["link"])
        continue

    print("Fetching Article...")
    content = get_article_content(post["link"])

    print("Content Length:", len(content))

    try:
        print("Rewriting with Gemini...")
        article = rewrite_article(post["title"], content)
    except Exception as e:
        print("Gemini Error:", e)
        continue

    print("Creating Draft...")

    draft = create_draft(
        post["title"],
        article
    )

    print("✅ Draft Created:", draft["id"])

    # Save processed link
    mark_processed(post["link"])

    print("✅ Saved to processed.json")
