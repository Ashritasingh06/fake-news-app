# 📰 Fake News Detection App

NLP web app that classifies news as Fake or Real using a fine-tuned 
RoBERTa transformer model. Deployed live on Streamlit Cloud.

🔗 Live Demo: https://fake-news-app-qvdamxtygbapbpadp5yh6g.streamlit.app/

## Tech Stack
- Language: Python
- NLP Model: RoBERTa (fine-tuned for fake news classification)
- Framework: Hugging Face Transformers
- Deep Learning: PyTorch
- Deployment: Streamlit Cloud

## How It Works
1. User pastes any news text
2. Text passed through fine-tuned RoBERTa model
3. Returns Fake / Real prediction with confidence score

## Run Locally
pip install -r requirements.txt
streamlit run app.py

## Author
Ashrita Singh | https://www.linkedin.com/in/ashrita-singh
