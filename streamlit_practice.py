import streamlit as st

# Set the app title
st.title("Sentiment Analyisis App")
st.write(
    "A simple machine learning app to predict the sentiment of a movie's review"
)

title = st.text_input('Movie title')
st.write("Input Text: ", title)