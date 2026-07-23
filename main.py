from modules.rss import get_latest_posts
from modules.scraper import get_article_content
from modules.ai import rewrite_article

RSS_FEEDS = [
    "https://www.karmasandhan.com/feed/",
]

posts = get_latest_posts(RSS_FEEDS[0], limit=1)

post = posts[0]

print("Fetching Article...")

content = get_article_content(post["link"])

print("Rewriting with AI...")

article = rewrite_article(
    post["title"],
    content
)

print(article)
