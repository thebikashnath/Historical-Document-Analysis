import streamlit as st
from analyzer import analyze_text, summarize_text

st.set_page_config(page_title="Historical Document Analysis", page_icon="📜")

st.title("📜 Historical Document Analysis")
st.write("Upload or paste historical text to explore common words, named entities, and summary.")

# File uploader and text area
uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
text_input = st.text_area("Or paste text here:")

# Demo mode button
if st.button("💡 Show Demo with Sample Text"):
    try:
        with open("sample_texts/declaration_of_independence.txt", "r", encoding="utf-8") as f:
            text = f.read()
        st.info("📄 Using sample text: Declaration of Independence")
    except FileNotFoundError:
        text = None
        st.warning("Sample text not found. Please make sure the file exists.")
else:
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
    elif text_input:
        text = text_input
    else:
        text = None

# Perform analysis
if text:
    common_words, entities = analyze_text(text)

    st.subheader("🔠 Most Common Words")
    for word, count in common_words:
        st.write(f"{word}: {count}")

    st.subheader("🏷️ Named Entities")
    for entity, label in entities:
        st.write(f"{entity} ({label})")

    st.subheader("📝 Summary")
    summary = summarize_text(text)
    st.write(summary)
