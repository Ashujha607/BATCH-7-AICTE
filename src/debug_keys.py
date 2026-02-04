from openai import OpenAI
import os

import toml

secrets = toml.load(".streamlit/secrets.toml")
key = secrets.get("GROK_API_KEY") or secrets.get("GEMINI_API_KEY") or "UNKNOWN"

print(f"Testing Key: {key[:10]}... with different providers\n")

# 1. Testing xAI (Grok) - Correct for this key prefix
print("--- 1. Testing xAI (api.x.ai) ---")
try:
    client = OpenAI(api_key=key, base_url="https://api.x.ai/v1")
    client.chat.completions.create(
        model="grok-beta",
        messages=[{"role": "user", "content": "Hi"}]
    )
    print("✅ Success!")
except Exception as e:
    print(f"❌ Failed (Expected if no credits): {e}")

print("\n")

# 2. Testing Groq (api.groq.com) - User's snippet suggested this
print("--- 2. Testing Groq (api.groq.com) ---")
try:
    client = OpenAI(api_key=key, base_url="https://api.groq.com/openai/v1")
    client.chat.completions.create(
        model="llama3-8b-8192", # Common Groq model
        messages=[{"role": "user", "content": "Hi"}]
    )
    print("✅ Success!")
except Exception as e:
    print(f"❌ Failed (Expected, key format mismatch): {e}")
