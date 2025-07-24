from dotenv import load_dotenv
import os
from langchain_community.embeddings import HuggingFaceEmbeddings 

# Load environment variables
load_dotenv()

# Initialize embedding model
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Example documents
documents = [
    "AI agents are software systems that use artificial intelligence",
    "to autonomously perform tasks and achieve goals on behalf of users."
]

# Get vector embeddings
vector = embedding.embed_documents(documents)

# Print the vectors
print(vector)
