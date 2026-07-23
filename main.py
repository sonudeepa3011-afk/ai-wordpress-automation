import os

print("AI WordPress Automation Started...")

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("✅ Gemini API Key Found")
else:
    print("❌ Gemini API Key Not Found")
