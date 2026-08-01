import os
import json
import google.generativeai as genai

# ---------------------------------------
# Configure Gemini
# ---------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# ---------------------------------------
# Prompt
# ---------------------------------------

SYSTEM_PROMPT = """
You are BookForge AI.

You are NOT a writer.

You are a professional publishing house.

Your job is to organize a manuscript.

Read the complete manuscript carefully.

Automatically detect:

1. Book Title (if title not given)

2. Subtitle

3. Genre

4. Writing Tone

5. Target Audience

6. Number of Chapters

7. Chapter Titles

8. Headings

9. Sub Headings

10. Important Notes

11. Bullet Lists

12. Definitions

13. Quotes

14. Examples

15. Summary

16. Conclusion

Do NOT rewrite.

Do NOT shorten.

Only organize.

Return ONLY valid JSON.

JSON Format:

{
"title":"",
"subtitle":"",
"genre":"",
"tone":"",
"audience":"",
"summary":"",
"chapters":[
{
"title":"",
"sections":[
{
"heading":"",
"subheading":"",
"content":""
}
]
}
]
}

NO markdown.

NO explanation.

ONLY JSON.
"""


# ---------------------------------------
# Analyze Book
# ---------------------------------------

def analyze_book(raw_text):

    prompt = SYSTEM_PROMPT + "\n\n" + raw_text

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")

    return json.loads(text)
