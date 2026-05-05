"""
gemini_review.py

Sends the full content of AlignED Research Report 3 (all HTML pages and JSON data files)
to the Gemini 2.5 Flash API for an expert peer review.

Uses the REST API directly via requests (no google-genai library needed).
Saves the review output to GEMINI_REVIEW.md in the same directory.

Parameters:
    None — all paths and keys are configured in the constants below.

Returns:
    Saves review text to GEMINI_REVIEW.md and prints it to stdout.
"""

import requests
import json
import sys
import os

# python-dotenv lets us read a local .env file (which is gitignored) so the
# API key never has to live inside this script. Install with: pip install python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv is optional; if it's not installed we just rely on real
    # environment variables set in the shell.
    pass

# -----------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------

# Load the API key from the environment. Set GOOGLE_API_KEY before running,
# e.g. via a local .env file (see .env.example) loaded by your shell, or:
#     export GOOGLE_API_KEY="..."   (bash)
#     $env:GOOGLE_API_KEY="..."     (PowerShell)
API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    sys.exit(
        "ERROR: GOOGLE_API_KEY environment variable is not set. "
        "Set it before running this script (see .env.example)."
    )

MODEL = "gemini-2.5-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
OUTPUT_PATH = r"C:\Users\trgal\projects\AlignED-research-report-3\GEMINI_REVIEW.md"
REPORT_DIR = r"C:\Users\trgal\projects\AlignED-research-report-3"

# -----------------------------------------------------------------------
# Load all HTML pages
# -----------------------------------------------------------------------

html_files = [
    "index.html",
    "introduction.html",
    "methods.html",
    "results.html",
    "discussion.html",
    "appendices.html",
]

html_content = ""
for filename in html_files:
    filepath = os.path.join(REPORT_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        html_content += f"\n\n=== FILE: {filename} ===\n"
        html_content += f.read()

# -----------------------------------------------------------------------
# Load all JSON data files
# -----------------------------------------------------------------------

data_dir = os.path.join(REPORT_DIR, "data")
json_files = [
    "key_metrics.json",
    "use_case_split.json",
    "collaboration_patterns.json",
    "subsector_patterns.json",
    "success_rates.json",
    "geographic.json",
    "consumer_vs_api.json",
]

json_content = ""
for filename in json_files:
    filepath = os.path.join(data_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        json_content += f"\n\n=== DATA FILE: {filename} ===\n"
        json_content += f.read()

# -----------------------------------------------------------------------
# Assemble the full payload text
# -----------------------------------------------------------------------

full_payload = (
    "=== HTML PAGES ===\n"
    + html_content
    + "\n\n=== JSON DATA FILES ===\n"
    + json_content
)

# -----------------------------------------------------------------------
# System prompt for peer review
# -----------------------------------------------------------------------

system_prompt = (
    "You are an expert peer reviewer in educational research methodology, "
    "data science, and scientific communication. You are reviewing AlignED "
    "Research Report 3, a descriptive analysis of 152,088 education-related "
    "Claude.ai conversations from the Anthropic Economic Index V4.\n\n"
    "Conduct a thorough peer review covering:\n\n"
    "1. Epistemic integrity: Does the report maintain appropriate humility "
    "about what the data can show? Are there any overclaims?\n"
    "2. Methodological issues: Are limitations adequate? Any gaps?\n"
    "3. Data accuracy: Check all stated numbers for internal consistency.\n"
    "4. Writing quality: Check for AI slop phrases, British/Australian "
    "spelling, clarity.\n"
    "5. Structural issues: Any broken references, missing content, logical gaps?\n"
    "6. What's missing: Important findings or alternative interpretations "
    "not covered?\n\n"
    "Rate each area and provide a ranked list of recommended changes. "
    "Be specific with file names and quote problematic text."
)

# -----------------------------------------------------------------------
# Build the API request body
# Increase maxOutputTokens to 16384 to get the full review.
# -----------------------------------------------------------------------

request_body = {
    "system_instruction": {
        "parts": [
            {"text": system_prompt}
        ]
    },
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": (
                        "Please conduct a full peer review of the following report. "
                        "The complete content of all HTML pages and JSON data files "
                        "is provided below.\n\n"
                        + full_payload
                    )
                }
            ]
        }
    ],
    "generationConfig": {
        "temperature": 0.3,
        "maxOutputTokens": 16384
    }
}

# -----------------------------------------------------------------------
# Send the request
# -----------------------------------------------------------------------

print(f"Sending request to Gemini API ({MODEL})...")
print(f"Payload size: {len(full_payload):,} characters")

response = requests.post(
    ENDPOINT,
    params={"key": API_KEY},
    headers={"Content-Type": "application/json"},
    json=request_body,
    timeout=180
)

# -----------------------------------------------------------------------
# Handle the response
# -----------------------------------------------------------------------

if response.status_code != 200:
    print(f"\nERROR: API returned status {response.status_code}")
    print(response.text)
    sys.exit(1)

response_data = response.json()

# Show diagnostics
for candidate in response_data.get("candidates", []):
    finish_reason = candidate.get("finishReason", "unknown")
    print(f"Finish reason: {finish_reason}")

usage = response_data.get("usageMetadata", {})
print(f"Input tokens: {usage.get('promptTokenCount', 'N/A')}")
print(f"Output tokens: {usage.get('candidatesTokenCount', 'N/A')}")

# Extract the generated text from the response structure
try:
    review_text = response_data["candidates"][0]["content"]["parts"][0]["text"]
    print(f"Review text length: {len(review_text):,} characters")
except (KeyError, IndexError) as e:
    print(f"\nERROR: Could not parse response structure: {e}")
    print("Full response (first 3000 chars):")
    print(json.dumps(response_data, indent=2)[:3000])
    sys.exit(1)

# -----------------------------------------------------------------------
# Save the review to GEMINI_REVIEW.md
# -----------------------------------------------------------------------

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("# Gemini Peer Review — AlignED Research Report 3\n\n")
    f.write("**Model:** gemini-2.5-flash  \n")
    f.write("**Date:** March 2026  \n")
    f.write("**Report:** AI and Education: What 152,000 Conversations Reveal\n\n")
    f.write("---\n\n")
    f.write(review_text)

print("\n" + "=" * 60)
print("GEMINI REVIEW OUTPUT")
print("=" * 60 + "\n")
print(review_text)
print("\n" + "=" * 60)
print(f"Review saved to: {OUTPUT_PATH}")
