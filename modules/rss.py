import feedparser

def get_latest_posts(feed_url, limit=5):
    feed = feedparser.parse(feed_url)

    # Debug
    print("Feed Status:", getattr(feed, "status", "Unknown"))
    print("Feed Bozo:", feed.bozo)

    if feed.bozo:
        print("Feed Error:", feed.bozo_exception)

    posts = []

    for entry in feed.entries[:limit]:
        posts.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", "")
        })

    return posts
