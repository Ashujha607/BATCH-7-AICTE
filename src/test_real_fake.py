import joblib
import re

# Load the vectorizer and new model
pipe = joblib.load("outputs/pipeline.joblib")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.strip()

# A distinctively REAL news headline (style-wise: formal, specific, neutral)
real_text = "U.S. officials announce new regulations on deep sea fishing to protect endangered species."
# A distinctively FAKE news headline (style-wise: clickbaity, emotional, vague)
fake_text = "BREAKING: Aliens found in New York subway eating pizza! You won't believe your eyes!"

def test(t):
    prob = pipe.predict_proba([clean_text(t)])[0, 1]
    print(f"Text: '{t}'")
    print(f"Fake Prob: {prob:.4f}")
    if prob < 0.5:
        print("Result: REAL ✅")
    else:
        print("Result: FAKE ❌")
    print("-" * 30)

test(real_text)
test(fake_text)
