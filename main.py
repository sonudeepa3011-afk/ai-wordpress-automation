from modules.rss import get_latest_posts

RSS_FEEDS = [
    "https://www.karmasandhan.com/feed/",
]

print("Reading:", RSS_FEEDS[0])

posts = get_latest_posts(RSS_FEEDS[0], limit=1)

print("Posts:", posts)
print("Count:", len(posts))

article = rewrite_article(
    post["title"],
    content
)

print(article)
