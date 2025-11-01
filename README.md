📜 Historical Document Analysis Tool

This Python-based project provides a simple yet effective framework for performing linguistic and sentiment analysis on historical texts. It's designed to help researchers quickly identify key concepts and emotional tone within documents.

Key Features

Text Preprocessing: Cleans raw text by converting it to lowercase, removing punctuation, and filtering out common stop words using NLTK.

Word Frequency Analysis: Identifies and ranks the Top 15 most frequent non-stop words to highlight dominant themes.

Sentiment Scoring: Utilizes the VADER model to calculate positive, negative, neutral, and overall compound sentiment scores for the document.

Visualization: Generates a bar chart (word_frequency_plot.png) of the top terms for quick visual interpretation.

🚀 Getting Started

Follow these steps to set up and run the analysis on your machine.

Prerequisites

You need Python 3.x installed. The required libraries are listed in requirements.txt.

Installation

Clone the Repository:

git clone [https://github.com/your-username/Historical-Document-Analysis.git](https://github.com/thebikashnath/Historical-Document-Analysis.git)

cd Historical-Document-Analysis


Install Dependencies:

pip install -r requirements.txt


Running the Analysis

Execute the main script from your terminal:

python analysis.py

