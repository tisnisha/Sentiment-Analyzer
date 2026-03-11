import streamlit as st
from transformers import pipeline

analyzer= pipeline("sentiment-analysis")

st.title("🧠Sentiment Analyzer")
st.write("Type any text below and the AI will tell you if it's positive or negative!")

user_input=st.text_area("Enter any text here: ")

if st.button("Analyse"):
    if user_input == "":
        st.warning("Please enter some text first!")
    else:
        result=analyzer(user_input)
        label=result[0]["label"]
        score=result[0]["score"]
        confidence = round(score * 100, 2)
       
        if label == "POSITIVE":
            st.success(f"✅ Sentiment: {label}")
        else:
            st.error(f"❌ Sentiment: {label}")

        st.write(f"Confidence: {confidence}%")
        st.progress(score)



