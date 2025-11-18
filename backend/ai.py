import json, re
from openai import OpenAI

# --------------------------------------------------
# 🔑 YOUR API KEY — PASTE BETWEEN THE QUOTES
OPENAI_API_KEY = "PASTE_KEY_HERE"
# --------------------------------------------------

# Fail-safe check
if not OPENAI_API_KEY or OPENAI_API_KEY == "PASTE_KEY_HERE":
    print("\n ERROR: OpenAI key missing! Edit ai.py and paste your key.\n")
    client = None
else:
    client = OpenAI(api_key=OPENAI_API_KEY)

def safe_json_extract(text: str):
    try:
        return json.loads(text)
    except:
        pass

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except:
            pass

    return {
        "title": "Test Plan",
        "description": "JSON format was invalid; fallback data used",
        "steps": [
            "Review document manually",
            "Fix invalid AI response format",
            "Try re-generating test steps"
        ]
    }

def generate_steps(text: str, max_steps: int = 10):
    if not client:
        return {
            "title": "AI Disabled",
            "description": "No API key found — functionality limited",
            "steps": ["Cannot generate steps without API key"]
        }

    prompt = f"""
    Analyze the following document and return ONLY valid JSON:

    {{
      "title": "string",
      "description": "string",
      "steps": ["step 1", "step 2", ... up to {max_steps}]
    }}

    Rules:
    - No markdown
    - No commentary outside JSON
    - No backticks
    - No code blocks
    - No explanations

    Document:
    {text}
    """

    response = client.responses.create(model="gpt-4.1-mini", input=prompt)
    raw_output = response.output_text.strip()
    return safe_json_extract(raw_output)
