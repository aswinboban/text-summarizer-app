import streamlit as st
from transformers import pipeline

# Set the page configuration at the top
st.set_page_config(page_title="AI Text Summarizer", layout="centered")

# Load the summarizer model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

# Load the model
summarizer = load_summarizer()

# Title of the app
st.title("AI Text Summarizer")

# Text area to input the document for summarization
text_input = st.text_area("Enter Text to Summarize:")

# Process the input text if provided
if text_input:
    with st.spinner('Summarizing the text...'):
        # Summarize the input text
        summary = summarizer(text_input)
        
        # Display the summary
        st.write("### Summary:")
        st.write(summary[0]['summary_text'])

# Instructions for the user
st.markdown("""
    **How to use:**
    - Paste your text in the input box above.
    - The AI will generate a summary based on the content.
""")

