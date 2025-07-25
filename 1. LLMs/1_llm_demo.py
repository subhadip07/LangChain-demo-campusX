from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the LLM
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke the model
result = llm.invoke("What is the capital of India?")

# Print the response
print(result)
