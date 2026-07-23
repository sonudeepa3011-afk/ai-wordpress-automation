import feedparser

def get_latest_posts(feed_url, limit=5):
    feed = feedparser.parse(feed_url)

    # Debug
    print("Feed Status:", getattr(feed, "status", "Unknown"))
    print("Feed Bozo:", feed.bozo)

    if feed.bozo:
        print("Feed Error:", feed.bozo_exception)

    posts = []

    for entry in feed.entries:
        title = entry.get("title", "").strip()
        link = entry.get("link", "").strip()
        published = entry.get("published", "")

        # Skip invalid entries
        if not title or not link:
            continue

        posts.append({
            "title": title,
            "link": link,
            "published": published
        })

        # Stop after required limit
        if len(posts) >= limit:
            break

    print("Valid Posts:", len(posts))

    return posts
