#!/usr/bin/env python3
import os
import argparse
from pathlib import Path
import re
import joblib
import streamlit as st
from openai import OpenAI

# --------------------------------------------------------------------------
# 1. AI Setup (Groq/Universal Mode)
# --------------------------------------------------------------------------
def configure_ai():
    api_key = None
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
    
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key or api_key.startswith("PASTE"):
        return None

    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

client_ai = configure_ai()

def get_ai_model():
    try:
        model = st.secrets.get("GROQ_MODEL")
        if model:
            return model
    except Exception:
        pass
    return os.getenv("GROQ_MODEL")

def ai_check(text):
    if not client_ai:
        return None
    
    preferred_model = get_ai_model()
    candidate_models = [
        preferred_model,
        "qwen/qwen3.8-27b",
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "openai/gpt-oss-120b",
    ]
    models_to_try = [m for i, m in enumerate(candidate_models) if m and m not in candidate_models[:i]]
    
    last_error = None
    for model_name in models_to_try:
        try:
            completion = client_ai.chat.completions.create(
                model=model_name,
                messages=[
                    # Updated Prompt: structured verdict + bilingual conclusion
                    {"role": "system", "content": "You are a STRICT fact-checker. Analyze the claim.\nFormat your response EXACTLY like this:\nVERDICT: [FAKE or REAL]\nCONCLUSION (English): [3-4 lines of evidence and reasoning in English]\nCONCLUSION (Hinglish): [3-4 lines of evidence and reasoning in Hinglish/Hindi]."},
                    {"role": "user", "content": f"Analyze strictly: '{text}'."}
                ]
            )
            msg = completion.choices[0].message
            content = msg.content
            if not content and hasattr(msg, "reasoning_content") and msg.reasoning_content:
                content = msg.reasoning_content
            if content and content.strip():
                return content
        except Exception as e:
            last_error = e
            continue

    return f"AI Analysis failed: {last_error}"

# --------------------------------------------------------------------------
# 2. Text Cleaning & Model Loading (Kept for backend but unused in simple UI)
# --------------------------------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.strip()

def project_root() -> Path:
    return Path(__file__).resolve().parents[1]

def load_models():
    root = project_root()
    out = root / "outputs"
    try:
        pipe = joblib.load(out / "pipeline.joblib")
        return pipe
    except:
        return None

# --------------------------------------------------------------------------
# 3. Streamlit UI Logic (Modern Overhaul)
# --------------------------------------------------------------------------
def main():
    st.set_page_config(
        page_title="Veritas | AI Fact Checker", 
        page_icon="🛡️", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS INJECTION ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Clean Background */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: white;
        }

        /* Input Area Styling */
        .stTextArea textarea {
            border-radius: 12px;
            background-color: #334155;
            border: 1px solid #475569;
            color: #f8fafc;
            padding: 1rem;
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }
        .stTextArea textarea:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.4);
        }

        /* Button Styling */
        .stButton>button {
            width: 100%;
            border-radius: 12px;
            background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            font-weight: 600;
            padding: 0.75rem 1rem;
            border: none;
            transition: transform 0.1s ease;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }

        /* Result Cards */
        .result-card {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 2rem;
            margin-top: 1rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            height: 100%;
        }
        
        .verdict-fake {
            color: #ef4444;
            font-weight: 800;
            font-size: 1.5rem;
            text-transform: uppercase;
        }
        .verdict-real {
            color: #10b981;
            font-weight: 800;
            font-size: 1.5rem;
            text-transform: uppercase;
        }
        
        /* Progress Bar */
        .stProgress > div > div > div > div {
            background-image: linear-gradient(90deg, #ef4444, #f59e0b);
            border-radius: 10px;
        }
        
        /* Hide Streamlit Bloat */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    col_logo, col_title = st.columns([1, 6])
    with col_logo:
        st.markdown("# 🛡️") 
    with col_title:
        st.markdown("# **Veritas** \n### *The Truth Engine*")

    st.markdown("---")

    # --- MAIN INPUT ---
    # Centered Layout
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        txt = st.text_area(
            "Enter claim to verify:", 
            height=200, 
            placeholder="e.g. 'NASA admitted the moon landing was filmed in a studio...'"
        )
        analyze = st.button("🔎 VERIFY TRUTH")

    # --- ANALYSIS LOGIC ---
    if analyze and txt.strip():
        # Load Model (Fixing NameError)
        pipe = load_models()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("## 🔍 Analysis Results")
        
        with st.spinner("Analyzing Evidence..."):
            ai_res = ai_check(txt)

        if ai_res:
            # 2. FACT CHECK (Intelligence Check) - Now Centered
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("### 🤖 Intelligence Check")
            st.caption("Cross-references claims with knowledge base.")
            
            # Parse AI Result
            if "VERDICT: FAKE" in ai_res:
                ai_color = "#ef4444"
                border_color = "#ef4444"
            elif "VERDICT: REAL" in ai_res:
                ai_color = "#10b981"
                border_color = "#10b981"
            else:
                ai_color = "#f59e0b"
                border_color = "#f59e0b"
            
            # Clean up formatting for visual display
            formatted_res = ai_res.replace("VERDICT:", "**VERDICT**:")
            formatted_res = formatted_res.replace("CONCLUSION (English):", "\n\n**CONCLUSION (English)**:")
            formatted_res = formatted_res.replace("CONCLUSION (Hinglish):", "\n\n**CONCLUSION (Hinglish)**:")
            
            st.markdown(f"<div style='border-left: 4px solid {border_color}; padding-left: 1rem; color: #e2e8f0;'>{formatted_res}</div>", unsafe_allow_html=True)
                
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("AI Analysis failed. Please check API Key.")

if __name__ == "__main__":
    main()