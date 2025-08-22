# Azure OpenAI Streamlit Chatbot

A simple **Streamlit web app** that allows you to chat with an AI using **Azure OpenAI Service**.  
This project demonstrates how to connect a frontend UI (Streamlit) with Azure GPT models for real-time Q&A.

---

## 🚀 Features
- Interactive web interface built with Streamlit
- Connects securely to Azure OpenAI GPT models
- Responds to user input in real-time
- Clean and minimal UI
- Easy to run locally or deploy online

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – Frontend UI
- **Azure OpenAI** – GPT-4/GPT-3.5 models

---

## 💻 Setup and Run Locally

1. Clone the repository:
```bash
git clone https://github.com/PranamyaShetty/azure-openai-streamlit.git
cd azure-openai-streamlit

2.Install dependencies:

pip install -r requirements.txt

3. Set your Azure OpenAI credentials:

Create a .streamlit/secrets.toml file (do not commit this):

AZURE_OPENAI_KEY = "your_azure_openai_key"
AZURE_OPENAI_ENDPOINT = "https://your-resource-name.openai.azure.com/"

4. Run the Streamlit app:

streamlit run app.py
