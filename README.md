import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Ensure necessary NLTK data is downloaded (only runs if not already present)
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords', quiet=True)
except LookupError:
    nltk.download('punkt', quiet=True)


def load_text(filepath):
    """Loads the historical document from the specified file path."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def preprocess_text(text):
    """Tokenizes the text and removes punctuation and stopwords."""
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text
    words = word_tokenize(text)
    
    # Define English stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    punctuations = ['(', ')', ':', ',', '.', ';', '“', '”', "'s", '?', '!', '--', '-', '’', '‘', '—', ':', '"']
    
    # Filter out stopwords and punctuation
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words and word not in punctuations]
    
    return filtered_words

def analyze_document(text_data):
    """Performs linguistic and sentiment analysis on the document."""
    
    # 1. Linguistic Analysis (Word Frequency)
    filtered_words = preprocess_text(text_data)
    fdist = FreqDist(filtered_words)
    
    print("\n--- 1. Top 15 Most Frequent Words (excluding stopwords) ---")
    top_words_df = pd.DataFrame(fdist.most_common(15), columns=['Word', 'Frequency'])
    print(top_words_df.to_markdown(index=False))

    # Save visualization of word frequency
    plt.figure(figsize=(10, 6))
    fdist.plot(15, cumulative=False, title='Top 15 Word Frequencies')
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig('word_frequency_plot.png')
    print("\n✅ Saved word frequency plot to 'word_frequency_plot.png'")

    # 2. Sentiment Analysis (VADER)
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text_data)
    
    print("\n--- 2. Sentiment Analysis (VADER Scores) ---")
    print(f"  Compound Score: {vs['compound']:.4f}")
    print(f"  Positive Score: {vs['pos']:.4f}")
    print(f"  Negative Score: {vs['neg']:.4f}")
    print(f"  Neutral Score:  {vs['neu']:.4f}")

    # Interpretation based on compound score
    if vs['compound'] >= 0.05:
        sentiment = "Positive"
    elif vs['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"\nOverall Document Sentiment: {sentiment}")
    print("\nAnalysis Complete!")


if __name__ == "__main__":
    DOCUMENT_PATH = 'historical_text.txt'
    
    print(f"Loading document from: {DOCUMENT_PATH}")
    document_text = load_text(DOCUMENT_PATH)
    
    if document_text:
        analyze_document(document_text)
