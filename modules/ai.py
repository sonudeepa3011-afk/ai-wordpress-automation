import os
import time
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

PROMPT = """
You are a professional news writer.

Rewrite the following news article.

Rules:
- 100% unique
- Human written
- SEO optimized
- Google Discover friendly
- Keep all facts
- Simple English
- Proper H2 and H3 headings
- Short paragraphs
- No promotional text
- No source website name
- End with a conclusion

Title:
{title}

Article:
{content}
"""


def rewrite_article(title, content):

    # Prevent very large prompts
    if len(content) > 12000:
        content = content[:12000]

    prompt = PROMPT.format(
        title=title,
        content=content
    )

    for attempt in range(1, 4):

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            article = ""

            if hasattr(response, "text") and response.text:
                article = response.text.strip()

            if len(article) < 500:
                raise Exception("Generated article too short.")

            print("✅ AI Rewrite Success")

            return article

        except Exception as e:

            print(f"Gemini Attempt {attempt}/3 Failed")
            print(e)

            error = str(e).lower()

            # Stop immediately if quota exceeded
            if "429" in error or "resource_exhausted" in error:
                raise Exception("Gemini quota exceeded.")

            if attempt < 3:
                print("Retrying in 5 seconds...")
                time.sleep(5)

    raise Exception("Gemini failed after 3 attempts.")
