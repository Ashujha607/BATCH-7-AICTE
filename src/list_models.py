import google.generativeai as genai
import os
import streamlit as st

# Mimic the app's key retrieval
api_key = "AIzaSyBslVAMbsgIK9ldWcZPLNIRCKk9QjmE94E"
genai.configure(api_key=api_key)

print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error listing models: {e}")
