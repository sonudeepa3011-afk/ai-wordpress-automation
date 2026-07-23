import os
import time
from google import genai


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


PROMPT = """
You are a professional news writer.

Rewrite the given article completely.

Rules:

- 100% unique content
- Human written
- SEO optimized
- Google Discover friendly
- Mobile friendly
- Do not copy sentences
- Keep all important facts
- Use simple English
- Create a catchy introduction
- Use proper H2 and H3 headings
- Use short paragraphs
- No horizontal lines
- No promotional text
- No source website name
- End with a short conclusion

Title:
{title}

Article:
{content}
"""


def rewrite_article(title, content):

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

            article = response.text.strip()

            if len(article) < 500:
                raise Exception("Generated article too short.")

            print("✅ AI Rewrite Success")

            return article

        except Exception as e:

            print(f"Gemini Attempt {attempt}/3 Failed")
            print(e)

            error = str(e).lower()

            if "429" in error or "resource_exhausted" in error:
                print("⚠ Gemini quota exceeded.")
                break

            if attempt < 3:
                print("Retrying in 5 seconds...")
                time.sleep(5)

    raise Exception("Gemini failed after 3 attempts.")
