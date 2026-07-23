from modules.rss import get_latest_posts
from modules.scraper import get_article_content
from modules.ai import rewrite_article

RSS_URL = "https://www.karmasandhan.com/feed/"

posts = get_latest_posts(RSS_URL, limit=1)

print("Posts:", len(posts))

if len(posts) == 0:
    raise Exception("RSS returned no posts.")

post = posts[0]

print("Title:", post["title"])
print("Fetching article...")

content = get_article_content(post["link"])

print("Article Length:", len(content))

print("Rewriting article...")

article = rewrite_article(post["title"], content)

print(article)
