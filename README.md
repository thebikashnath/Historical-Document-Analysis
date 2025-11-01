Founding Document Linguistics Analyzer

📜 Project Overview: Analyzing the U.S. Declaration of Independence

This Python project performs foundational Natural Language Processing (NLP) and Sentiment Analysis on a key historical document: an excerpt from the United States Declaration of Independence.

The goal is to demonstrate basic text analysis skills, including tokenization, stopword removal, word frequency analysis, and polarity scoring. This serves as a great, simple template for analyzing any historical text.

Key Features

Text Loading: Reads the document content from historical_text.txt.

Linguistic Analysis: Calculates the frequency distribution of words after cleaning.

Data Visualization: Generates a bar plot of the top 15 most frequent words (word_frequency_plot.png).

Sentiment Analysis: Uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) model to score the document's overall sentiment (Positive, Negative, Neutral).

🚀 Getting Started

Follow these steps to clone the project and run the analysis script locally.

1. Repository Setup (Simulated)

In a real GitHub project, you would first clone the repository:

# This is what you would run on a real GitHub repository
# git clone [https://github.com/YourUsername/Founding-Document-Linguistics-Analyzer.git](https://github.com/YourUsername/Founding-Document-Linguistics-Analyzer.git)
# cd Founding-Document-Linguistics-Analyzer


2. Environment Setup

This project requires Python 3.x and the packages listed in requirements.txt.

Create a Virtual Environment (Recommended):

python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# venv\Scripts\activate   # On Windows


Install Dependencies:

pip install -r requirements.txt


3. Run the Analysis

Execute the main Python script:

python analysis.py


4. Review Results

The script will print the Top 15 words and the Sentiment Scores to the console. It will also generate a file:

word_frequency_plot.png: A visualization of the most frequent words.

📝 Document and Analysis Details

The analysis is performed on the first two paragraphs of the U.S. Declaration of Independence.

Example Output Findings

Word

Frequency

government

3

people

2

bands

1

dissolve

1

political

1

...

...

Sentiment Analysis:

Compound Score: (Likely between 0.8 and 1.0, indicating a strong positive/persuasive tone despite grievances)

Overall Sentiment: Positive

The high positive score often reflects the use of strong, moral language ("unalienable Rights," "Safety and Happiness," "just powers") which VADER's dictionary classifies positively, even in a document that contains statements of complaint.

License: MIT License (or choose your preferred license)
Author: Your Name / Gemini Assistant