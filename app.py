import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detection App")
st.write("Enter any news article or headline to check if it's Real or Fake.")

@st.cache_resource
def load_model():
    return pipeline("text-classification", model="hamzab/roberta-fake-news-classification")

classifier = load_model()

text = st.text_area("Paste news text here", height=200)

if st.button("Analyze"):
    if text.strip():
        with st.spinner("Analyzing..."):
            result = classifier(text[:512])[0]
            label = result['label']
            score = round(result['score'] * 100, 2)
        if "FAKE" in label.upper():
            st.error(f"Prediction: FAKE NEWS | Confidence: {score}%")
        else:
            st.success(f"Prediction: REAL NEWS | Confidence: {score}%")
    else:
        st.warning("Please enter some text first.")
