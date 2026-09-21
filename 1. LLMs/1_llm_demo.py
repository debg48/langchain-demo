import warnings
warnings.filterwarnings("ignore")

import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3.1-flash-lite")

response = llm.invoke("What is the capital of India?")
print(response)