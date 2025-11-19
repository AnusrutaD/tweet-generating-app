import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

os.environ['GOOGLE_API_KEY'] = st.secrets('GOOGLE_API_KEY')

# Initialize googles Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-lite")

# Create Prompt template for generating tweets
# tweet_template = "create {number} of tweets on {topic}"
tweet_template = """You are an experienced social media content creator. Generate {number} engaging, creative, and concise tweets on the topic “{topic}”.
Rules:

Avoid controversial, political, sensitive, or negative content.

Maintain a friendly, positive, and helpful tone.

Keep each tweet under 280 characters.

Make the tweets unique and not repetitive.

No hashtags unless the topic naturally requires them.

No emojis unless adding them improves clarity.
"""
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ["number", "topic"])

tweet_template.format(number = 7, topic = "Submarine")

tweet_chain = tweet_prompt | gemini_model
# response = tweet_chain.invoke({"number": 5, "topic": "War in Middle East"})

st.header("🐦 Tweet Generator")

st.subheader("Generate Tweets using generative AI 🤖")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)