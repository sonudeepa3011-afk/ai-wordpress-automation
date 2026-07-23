import feedparser

def get_latest_posts(feed_url, limit=5):
    """
    RSS Feed se latest posts return karega.
    """

    feed = feedparser.parse(feed_url)

    posts = []

    for entry in feed.entries[:limit]:
        posts.append({
            "title": entry.title,
            "link": entry.link,
            "published": getattr(entry, "published", "")
        })

    return posts
