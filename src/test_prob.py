import joblib
import re

# Load the vectorizer and new model
vec = joblib.load("outputs/vectorizer.joblib")
model = joblib.load("outputs/model.joblib")
pipe = joblib.load("outputs/pipeline.joblib")

text = "The earth is flat and made of cheese."

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.strip()

print(f"Testing text: '{text}'")
prob = pipe.predict_proba([clean_text(text)])[0, 1]
print(f"Fake Probability: {prob:.4f}")
print(f"Prediction: {'FAKE' if prob > 0.5 else 'REAL'}")
