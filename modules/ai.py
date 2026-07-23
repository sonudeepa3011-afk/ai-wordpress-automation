import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def rewrite_article(title, content):

    prompt = f"""
Rewrite this article completely.

Rules:
- 100% Unique
- SEO Friendly
- Human Written

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
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text
