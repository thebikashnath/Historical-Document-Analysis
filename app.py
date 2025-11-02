from flask import Flask, request, render_template
import spacy
from textblob import TextBlob

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        text = request.form["document"]
        doc = nlp(text)
        result["entities"] = [(ent.text, ent.label_) for ent in doc.ents]
        result["keywords"] = [token.text for token in doc if token.is_alpha and not token.is_stop]
        result["sentiment"] = TextBlob(text).sentiment
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
