from flask import Flask, request, render_template
import spacy
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def generate_wordcloud(keywords):
    text = " ".join(keywords)
    wc = WordCloud(width=800, height=400, background_color="#fdf6e3", colormap="copper")
    wc.generate(text)
    wc.to_file("static/historical_wordcloud.png")

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        text = request.form.get("document", "")
        if "file" in request.files:
            file = request.files["file"]
            if file.filename.endswith(".txt"):
                text = file.read().decode("utf-8")

        if text.strip():
            doc = nlp(text)
            result["entities"] = [(ent.text, ent.label_) for ent in doc.ents]
            result["keywords"] = [token.text for token in doc if token.is_alpha and not token.is_stop]
            result["sentiment"] = TextBlob(text).sentiment
            generate_wordcloud(result["keywords"])

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
