from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os

# Azure OpenAI config
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
embed_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")

# 1. Load document
loader = TextLoader("sample_doc.txt")
docs = loader.load()

# 2. Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
chunks = splitter.split_documents(docs)

# 3. Embeddings
embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=endpoint,
    deployment=embed_deployment,
)

db = FAISS.from_documents(chunks, embeddings)

# 4. LLM
llm = AzureChatOpenAI(
    azure_endpoint=endpoint,
    deployment_name=deployment,
    temperature=0
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

query = "What are the key risks in the document?"
result = qa({"query": query})
print(result)
