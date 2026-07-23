import feedparser

feed_url = "https://www.karmasandhan.com/feed/"

feed = feedparser.parse(feed_url)

print("Total Posts:", len(feed.entries))

for post in feed.entries[:10]:
    print("TITLE :", post.title)
    print("LINK  :", post.link)
    print("-" * 50)
