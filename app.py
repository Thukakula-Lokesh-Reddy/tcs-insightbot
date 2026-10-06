'''
    REAL TIME JOB
    1.create a flask function that takes question from postman
    2.read the question from json
    3.load local faiss db
    4.ask the question to faiss db and get relevant chunks
    5.make a prompt with question and chunk
    6.pass prompt to gemini llm
    7.get response from gemini and return to postman or ui in json format
'''

from flask import Flask, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.route('/ask', methods=['POST'])
def f1():

    data = request.get_json()
    question = data.get('question')

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    my_vector_store = FAISS.load_local(
        "tcs_doc_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = my_vector_store.similarity_search(
        question,
        k=3
    )

    chunks = [i.page_content for i in docs]

    my_prompt = f'''
I am asking a question based on the TCS annual report pdf file.

Please answer the question based on the chunks provided below.

If the answer is not found in the chunks, please say "I don't know".

Do not make up an answer.

question: {question}

context: {chunks}
'''

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=my_prompt
    )

    return jsonify({
        "result": response.text
    })


if __name__ == "__main__":
    app.run()