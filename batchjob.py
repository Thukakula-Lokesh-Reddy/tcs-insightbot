'''
    BATCH JOB
    1. Load the TCS annual report PDF file and store it in the documents variable.
    2. Split the documents into chunks using RecursiveCharacterTextSplitter.
    3. Create embeddings for the chunks using HuggingFaceEmbeddings.
    4. Create a FAISS index and store the chunks in the vector database.
    5. Store the vector database permanently for future use.
'''
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import os
import faiss
from langchain_community.vectorstores import FAISS



# step1:Load the tcs pdf file and store it in documents variable
loader=PyPDFLoader("C:\\FinalGENaiProj_26\\TCSchatbot\\documents\\TCS_annual report.pdf")
documents=loader.load()

# step2: Split the documents into chunks 
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
    )
  #Now load chunks into mychunks variable
mychunks=text_splitter.split_documents(documents)
print(len(mychunks))

# Step3: Create embeddings for the chunks using HuggingFaceEmbeddingModel
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# step4: Create FAISS index and store documents
vector_store=FAISS.from_documents(documents=mychunks, embedding=embeddings)

# step 6:store vector store[db] permanently locally for future use
vector_store.save_local("tcs_doc_index")
print("successfully stored vector db permanently")


