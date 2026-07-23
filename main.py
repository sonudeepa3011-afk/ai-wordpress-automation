from modules.rss import get_latest_posts
from modules.scraper import get_article_content
from modules.ai import rewrite_article
from modules.wordpress import create_draft
from modules.duplicate import is_duplicate
from modules.state import already_processed, mark_processed

RSS_FEEDS = [
    {
        "name": "Karmasandhan",
        "url": "https://www.karmasandhan.com/feed/"
    },
    {
        "name": "SarkariResult",
        "url": "https://www.sarkariresult.com.cm/feed/"
    },
    {
        "name": "Buddy4Study",
        "url": "https://hindi.buddy4study.com/feed/"
    }
]

POSTS_PER_SOURCE = 2


def process_post(post):

    print("\n" + "=" * 60)
    print("Source :", post["source"])
    print("Title  :", post["title"])

    # Already processed
    if already_processed(post["link"]):
        print("⏭ Already Processed")
        return

    # Duplicate in WordPress
    if is_duplicate(post["title"]):
        print("⏭ Duplicate Found")
        mark_processed(post["link"])
        return

    print("Fetching Article...")

    content = get_article_content(post["link"])

    if not content:
        print("❌ Empty Article")
        return

    print("Content Length:", len(content))

    try:

        print("Rewriting with Gemini...")

        article = rewrite_article(
            post["title"],
            content
        )

    except Exception as e:

        print("Gemini Error:", e)
        return

    try:

        print("Creating Draft...")

        draft = create_draft(
            post["title"],
            article
        )

        print(f"✅ Draft Created : {draft['id']}")

        mark_processed(post["link"])

        print("✅ Saved to processed.json")

    except Exception as e:

        print("WordPress Error:", e)


def main():

    total_posts = 0

    for source in RSS_FEEDS:

        posts = get_latest_posts(
            source["url"],
            limit=POSTS_PER_SOURCE,
            source_name=source["name"]
        )

        total_posts += len(posts)

        for post in posts:
            process_post(post)

    print("\n" + "=" * 60)
    print(f"Automation Finished")
    print(f"Total Posts Fetched : {total_posts}")
    print("=" * 60)


if __name__ == "__main__":
    main()
