from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.llms.azure_openai import AzureOpenAI
import os

docs = SimpleDirectoryReader("docs").load_data()

embed_model = AzureOpenAIEmbedding(
    model="text-embedding",
    deployment_name=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
)

index = VectorStoreIndex.from_documents(docs, embed_model=embed_model)

query_engine = index.as_query_engine(
    llm=AzureOpenAI(
        model="gpt-4o-mini",
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        temperature=0
    )
)

response = query_engine.query("Summarize this document for executives")
print(response)
