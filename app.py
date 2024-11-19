import streamlit as st
from textblob import TextBlob     # sentiment analysis package
import plotly.graph_objects as go # data visualization package
    

st.markdown("# Welcome to my app!")

st.markdown("### Please enter some text below and press enter!")

st.markdown("### Hi prog2 saxa class!!")

def sent_app(text):

    # Extract sentiment
    sentiment_score = TextBlob(f"{text}").sentiment.polarity
    
    # Use score to assign label
    if sentiment_score > .15:
        label = "Positive"
    elif sentiment_score < -.15:
        label = "Negative"
    else:
        label = "Neutral"
    
    # Plot score on gauge plot
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = sentiment_score,
    title = {'text': f"Sentiment: {label}"},
    gauge = {"axis": {"range": [-1, 1]},
            "steps": [
                {"range": [-1, -.15], "color":"red"},
                {"range": [-.15, .15], "color":"gray"},
                {"range": [.15, 1], "color":"lightgreen"}
            ],
            "bar":{"color":"yellow"}}
    ))
    
    return st.plotly_chart(fig)

text = st.text_input("Enter text:", value = "Enter text here")

sent_app(text)
