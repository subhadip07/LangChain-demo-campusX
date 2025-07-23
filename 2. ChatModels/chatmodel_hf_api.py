from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load environment variables
load_dotenv()
# api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize chat-compatible endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# Create LangChain chat wrapper
chat_model = ChatHuggingFace(llm=llm)

# Invoke the model
response = chat_model.invoke("What is the capital of India")
print(response.content)
