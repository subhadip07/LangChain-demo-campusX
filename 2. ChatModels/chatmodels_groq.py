from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Get API key
api_key = os.getenv('GROQ_API_KEY')

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    api_key=api_key,
    temperature=1.5,
    max_completion_tokens=10)

# Invoke the model
result = llm.invoke("What is the capital of India?")

# Print the response
print(result.content)