

import os
import streamlit as st
from openai import AzureOpenAI

# Load key from environment
api_key = os.getenv("AZURE_OPENAI_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-02-01",
    azure_endpoint=endpoint
)


DEPLOYMENT_NAME = "gpt-35-turbo"   # 👈 use the deployment name from Azure portal


# ---- Streamlit App ----
st.set_page_config(page_title="Azure AI Chatbot", page_icon="🤖")

st.title("🤖 Azure OpenAI Chatbot")
st.write("Ask me anything!")

# Input box
user_input = st.text_input("Your message:")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response.choices[0].message.content
        st.success(bot_reply)
