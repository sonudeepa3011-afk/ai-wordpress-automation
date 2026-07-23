from modules.rss import get_latest_posts

RSS_FEEDS = [
    "https://www.karmasandhan.com/feed/",
]

for feed in RSS_FEEDS:
    print(f"\nReading Feed: {feed}\n")

    posts = get_latest_posts(feed)

    for post in posts:
        print("TITLE :", post["title"])
        print("LINK  :", post["link"])
        print("DATE  :", post["published"])
        print("-" * 60)
