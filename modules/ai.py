import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def rewrite_article(title, content):

    prompt = f"""
You are an SEO news writer.

Rewrite this article completely.

Rules:
- 100% Unique
- Human Written
- SEO Friendly
- Keep all facts correct
- Create a new attractive title
- Use H2 and H3 headings
- Mobile friendly paragraphs
- Do not copy sentences

Title:
{title}

Article:
{content}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text
