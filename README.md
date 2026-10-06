# TCS InsightBot — RAG-Powered Enterprise Chatbot

TCS InsightBot is a Retrieval-Augmented Generation (RAG) based question-answering chatbot that allows users to ask questions about the **TCS Annual Report**.

The application retrieves the most relevant information from the annual report using **FAISS vector search** and **Hugging Face sentence-transformer embeddings**, then uses **Google Gemini** to generate a natural-language answer based on the retrieved context.

---

## 🚀 Features

* Ask natural-language questions about the TCS Annual Report
* Retrieval-Augmented Generation (RAG) architecture
* PDF document processing and text chunking
* Semantic search using Hugging Face embeddings
* FAISS-based vector database for efficient similarity search
* Google Gemini for answer generation
* Flask REST API for handling user queries
* Postman support for API testing
* Context-based responses to reduce unsupported answers
* Local vector database persistence

---

## 🏗️ Project Architecture
'
                  TCS Annual Report PDF
                           |
                           v
                     batchjob.py
                           |
                           v
                    Text Chunking
                           |
                           v
              Hugging Face Embeddings
                           |
                           v
                    FAISS Vector DB
                           |
                           v
                    tcs_doc_index
                           |
                           |
                           v
                      app.py
                           |
                           v
                  User Question
                           |
                           v
                  Similarity Search
                           |
                           v
                  Relevant Documents
                           |
                           v
                    Context + Query
                           |
                           v
                     Google Gemini
                           |
                           v
                       Answer
                           |
                           v
                       Postman



## 🛠️ Technologies Used

| Technology            | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| Python                | Core programming language                        |
| Flask                 | REST API backend                                 |
| LangChain             | Document processing and vector store integration |
| Hugging Face          | Text embeddings                                  |
| Sentence Transformers | Semantic representation of text                  |
| FAISS                 | Vector similarity search                         |
| Google Gemini         | Large Language Model for answer generation       |
| Postman               | API testing                                      |
| PyPDF                 | PDF document loading                             |


## 📂 Project Structure


tcs-insightbot/
│
├── app.py
├── batchjob.py
├── .gitignore
│
├── documents/
│   └── TCS_annual report.pdf
│
└── tcs_doc_index/
    ├── index.faiss
    └── index.pkl


> The `.env` file containing the Gemini API key is intentionally excluded from the repository for security.

---

## 🔄 How It Works

### 1. Document Loading

The TCS Annual Report PDF is loaded using `PyPDFLoader`.

### 2. Text Chunking

The document is divided into smaller overlapping chunks using `RecursiveCharacterTextSplitter`.

This allows the system to retrieve relevant portions of the report instead of processing the entire document for every question.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector using:


sentence-transformers/all-mpnet-base-v2


These vectors represent the semantic meaning of the document content.

### 4. Vector Storage

The generated embeddings are stored in a **FAISS vector database**.

The vector database is persisted locally in:



### 5. Question Retrieval

When a user sends a question to the Flask API, the question is converted into an embedding and compared with the stored document vectors.

The application retrieves the **top 3 most relevant chunks**.

### 6. Prompt Construction

The retrieved chunks are combined with the user's question to create a context-based prompt.

The prompt instructs Gemini to answer using the retrieved information and avoid making up information when the answer is not available in the retrieved context.

### 7. Answer Generation

Google Gemini processes the question and retrieved context and generates the final natural-language response.

### 8. API Response

The generated answer is returned to the user as JSON through the Flask REST API.

---

## 🔌 API Usage

### Endpoint


POST /ask


### Request

Send a JSON request:

```json
{
    "question": "Who is the chairman of TCS?"
}
```

### Example Response

```json
{
    "result": "N. Chandrasekaran is the Chairman of Tata Consultancy Services (TCS)."
}
```

---

## 🧪 Testing with Postman

1. Start the Flask application.
2. Open Postman.
3. Select:

   ```text
   POST
   ```
4. Enter:

   ```text
   http://127.0.0.1:5000/ask
   ```
5. Select **Body → raw → JSON**.
6. Enter:

```json
{
    "question": "What is the revenue of TCS?"
}
```

7. Click **Send**.

The API returns the answer generated from the relevant information retrieved from the TCS Annual Report.

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Thukakula-Lokesh-Reddy/tcs-insightbot.git
```

Navigate into the project:

```bash
cd tcs-insightbot
```

### 2. Create a Virtual Environment

```bash
python -m venv Chatbotenv
```

Activate it on Windows:

```powershell
Chatbotenv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages used by the project:

```bash
pip install flask
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-huggingface
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
pip install python-dotenv
pip install google-genai
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Never commit your `.env` file or expose your API key publicly.**

### 5. Create the Vector Database

If the existing FAISS index is not available, run:

```bash
python batchjob.py
```

This processes the TCS Annual Report and creates the local FAISS vector database.

### 6. Start the Application

Run:

```bash
python app.py
```

The Flask API will start locally.

---

## 🔐 Security

Sensitive credentials are not stored in the source code.

The Gemini API key is loaded from an environment variable using `.env`.

The following files are excluded using `.gitignore`:

```text
.env
Chatbotenv/
__pycache__/
*.pyc
```

---

## 🎯 Use Cases

TCS InsightBot can be used for:

* Annual report question answering
* Enterprise document analysis
* Financial report exploration
* Semantic document search
* Knowledge-base assistants
* RAG-based question-answering systems

---

## 📈 Future Enhancements

Potential improvements include:

* Web-based chatbot interface
* Support for multiple company reports
* Conversation memory
* Source/page references in responses
* Improved document metadata handling
* Streaming responses
* Authentication and authorization
* Deployment using cloud platforms
* Evaluation metrics for RAG response quality

---

## 👨‍💻 Author

**T Lokesh Reddy**

GitHub:
https://github.com/Thukakula-Lokesh-Reddy

---

## 📄 License

This project is intended for educational and demonstration purposes.
