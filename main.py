from modules.rss import get_latest_posts
from modules.scraper import get_article_content

RSS_FEEDS = [
    "https://www.karmasandhan.com/feed/",
]

for feed in RSS_FEEDS:

    posts = get_latest_posts(feed, limit=1)

    for post in posts:

        print("TITLE :", post["title"])
        print("LINK  :", post["link"])

        print("\nFetching Article...\n")

        content = get_article_content(post["link"])

        print(content[:3000])
