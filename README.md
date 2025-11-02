# 📜 Historical Document Analyzer

An advanced NLP-powered web application that analyzes historical texts for **named entities, keywords, sentiment**, and generates a **word cloud visualization**.  
Built with **Flask, SpaCy, TextBlob, WordCloud, and Bootstrap**, styled with a parchment‑inspired theme to evoke the feel of archival research.

---

## ✨ Features

- 🔍 **Named Entity Recognition (NER)** — Extracts people, places, dates, and organizations  
- 🗝️ **Keyword Extraction** — Highlights important words in the text  
- 📈 **Sentiment Analysis** — Detects tone (positive, negative, neutral) with polarity & subjectivity scores  
- ☁️ **Word Cloud Visualization** — Generates a historical‑themed word cloud of keywords  
- 📁 **File Upload Support** — Upload `.txt` files for analysis  
- 🎨 **Historical UI** — Elegant parchment‑style background, serif fonts, and responsive Bootstrap layout  

---

## 🏗️ Project Structure

historical-doc-analyzer/ 
├── app.py 
├── requirements.txt
├── static/ │ 
├── images/ │ 
│ └── background.png # parchment-style background 
│ └── historical_wordcloud.png # generated word cloud 
├── templates/ 
│ └── index.html # main UI

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/historical-doc-analyzer.git
cd historical-doc-analyzer

2. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Download NLP models
bash
python -m textblob.download_corpora
python -m spacy download en_core_web_sm

🚀 Running Locally
bash
python app.py
Visit: http://127.0.0.1:5000/

🌐 Deployment on Render
In Render’s Build Command field, use:

bash
pip install -r requirements.txt && python -m textblob.download_corpora && python -m spacy download en_core_web_sm
In Start Command:

bash
gunicorn app:app
📦 Requirements
requirements.txt includes:

Code
flask
spacy
textblob
wordcloud
matplotlib
gunicorn

🧑‍💻 Author
Built with ❤️ by Bikash Inspired by archival research, powered by modern NLP.
