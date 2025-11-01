import spacy
from collections import Counter, defaultdict
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def analyze_text(text):
    doc = nlp(clean_text(text))
    tokens = [token.text.lower() for token in doc if token.is_alpha]
    common_words = Counter(tokens).most_common(10)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return common_words, entities

def summarize_text(text, max_sentences=5):
    text = clean_text(text)
    doc = nlp(text)
    
    words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    freq = Counter(words)
    
    sentence_scores = defaultdict(int)
    for sent in doc.sents:
        for token in sent:
            if token.text.lower() in freq:
                sentence_scores[sent] += freq[token.text.lower()]
    
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]
    summary = ' '.join([sent.text for sent in top_sentences])
    return summary
