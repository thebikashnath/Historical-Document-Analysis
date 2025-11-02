#!/bin/bash

echo "🔧 Setting up your Historical Document Analyzer environment..."

# Step 1: Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt

# Step 3: Download TextBlob corpora
echo "🧠 Downloading TextBlob corpora..."
python -m textblob.download_corpora

# Step 4: Download SpaCy English model
echo "🧠 Downloading SpaCy English model..."
python -m spacy download en_core_web_sm

echo "✅ Setup complete! You're ready to run the app with: python app.py"
