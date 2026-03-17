import streamlit as st
from transformers import pipeline

st.title("Fake News Detection App")

@st.cache_resource
def load_model():
    return pipeline("text-classification")

classifier = load_model()

text = st.text_area("Enter News Here")

if st.button("Check"):
    if text:
        result = classifier(text)[0]

        if result['label'] == "NEGATIVE":
            st.write("Prediction: FAKE")
        else:
            st.write("Prediction: REAL")

        st.write("Confidence:", round(result['score']*100, 2), "%")
    else:
        st.write("Please enter text")