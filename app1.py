from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Create FAISS vector store from documents (assuming already indexed)
vectorstore = FAISS.load_local("faiss_index", embeddings)

# Set up retrieval QA chain
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Example query
query = "Explain how Python for loops work."
answer = qa.run(query)
print(answer)
