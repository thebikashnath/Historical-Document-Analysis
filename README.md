📜 Historical Document Analysis

Analyze historical texts to discover common words, named entities, and summaries using NLP.

---

## 🚀 Run Locally

```bash
git clone https://github.com/thebikashnath/Historical-Document-Analysis.git
cd Historical-Document-Analysis
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
