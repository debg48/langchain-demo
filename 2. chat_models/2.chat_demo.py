import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite",temperature=0,max_output_tokens=50)

response = llm.invoke("Suggest me 5 names for a thriller story. Just give me names listing them is enough!")
print(response.content)