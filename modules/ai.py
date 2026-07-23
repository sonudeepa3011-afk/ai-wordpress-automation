import os
import time
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

PROMPT = """
Act as a **Premium SEO Content Writer, Government Job Expert, SEO Strategist, and Google Discover Specialist**.

I will provide you with the raw recruitment notification or official details. Convert it into a **high-quality, human-written, SEO-optimized Government Job article** that is designed to rank in **Google Search, Google Discover, Featured Snippets, and AI Overviews**.

# Writing Guidelines

* Write in simple, professional English.
* Maintain **E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)**.
* Avoid keyword stuffing and clickbait.
* Use short paragraphs and proper heading hierarchy (H2/H3).
* Target Featured Snippets and People Also Ask (PAA).
* Use Markdown formatting.
* Article should be easy to read on mobile devices.
* Use transition words and natural language.
* Write content in a human, conversational, and informative tone.
* Paragraphs should not exceed 3–4 lines.
* The article should be between **1,500–2,500 words**, depending on the notification details.
* Avoid unnecessary filler content.

# Formatting Rules (Very Important)

* Never use horizontal divider lines (`---`, `***`, `___`) anywhere in the article.
* Do not insert separators between sections, tables, FAQs, or the conclusion.
* Separate sections only by using proper headings and spacing.
* Use only H2 (`##`) and H3 (`###`) headings.
* Do not skip heading levels.
* The article must have a clean WordPress/GeneratePress-friendly layout.
* Do not generate decorative boxes, emojis, or extra symbols.
* Avoid excessive blank spaces.
* Keep all tables in simple Markdown format.
* Tables should be mobile-friendly and not overly wide.
* The article should look like a professionally published Government Job post.
* Output only the final publish-ready article.

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
