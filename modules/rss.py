import feedparser
import time


def get_latest_posts(feed_url, limit=5, source_name="Unknown"):

    print("\n" + "=" * 60)
    print(f"Source      : {source_name}")
    print(f"RSS Feed    : {feed_url}")
    print("=" * 60)

    for attempt in range(1, 4):

        try:
            feed = feedparser.parse(
                feed_url,
                agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )

            print("Feed Status :", getattr(feed, "status", "Unknown"))
            print("Feed Bozo   :", feed.bozo)

            if feed.bozo:
                print("Feed Error  :", feed.bozo_exception)

            if not feed.entries:
                print("❌ No posts found.")
                return []

            posts = []

            for entry in feed.entries:

                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()
                published = entry.get("published", "").strip()

                if not title or not link:
                    continue

                posts.append({
                    "source": source_name,
                    "title": title,
                    "link": link,
                    "published": published
                })

                if len(posts) >= limit:
                    break

            print(f"✅ Valid Posts : {len(posts)}")

            return posts

        except Exception as e:

            print(f"Attempt {attempt}/3 Failed")
            print(e)

            if attempt < 3:
                print("Retrying in 2 seconds...")
                time.sleep(2)

    print("❌ RSS Fetch Failed.")

    return []
