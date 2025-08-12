FAQ Chatbot with Ollama (LLaMA 3.1)

This project is a Streamlit-based chatbot that first tries to answer questions using a predefined FAQ knowledge base. If a suitable FAQ match is found, the answer is displayed instantly. If the user is not satisfied with the FAQ answer, they can click a button to ask the AI (LLaMA 3.1) for a more detailed or conversational response.

The app uses Ollama for local AI inference, ensuring fast, private, and cost-free responses without relying on external APIs.

🚀 Features
📄 FAQ First Approach – Instantly answers from a predefined FAQ dataset using semantic search.

🤖 Ask AI if Not Satisfied – Allows the user to get a custom LLaMA 3.1 AI answer if the FAQ is insufficient.

💾 Chat History – Keeps the full conversation context for AI to refer back to previous messages.

🔍 Intelligent Matching – Uses vector similarity search to find the most relevant FAQ.

💡 Local AI Inference – Powered by Ollama and LLaMA 3.1 for privacy and speed.

🎨 Clean UI – Built with Streamlit for a simple, interactive interface.

🖱 Enter Key or Button – Ask questions by pressing Enter or clicking "Ask".

📂 Project Structure
graphql
Copy
Edit
chatbot/
│
├── app.py                 # Main Streamlit application
├── faqs.json              # Predefined FAQ knowledge base
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/chatbot.git
cd chatbot

2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install & Run Ollama
Follow the instructions to install Ollama from:
https://ollama.ai/download

Pull the LLaMA 3.1 model:
ollama pull llama3.1

▶️ Usage
Run the app:

streamlit run app.py
🛠 How It Works
User asks a question via the input box.

FAQ Search:

The question is compared against all FAQ questions using a similarity score.

If the similarity is above a threshold, the FAQ answer is shown instantly.

Ask AI Option:

If the FAQ answer is not sufficient, the user can click "Ask AI" to send the query to the LLaMA 3.1 model.

AI Response:

The AI responds in a conversational manner, using the entire chat history for better context.

📌 Example FAQ Flow
User: What is the minimum balance for a savings account?
Bot (FAQ): The minimum balance required is ₹10,000.
[Ask AI] (button appears)

User clicks "Ask AI"
Bot (AI): The minimum balance for our savings account is ₹10,000, but we also offer zero-balance accounts for students and senior citizens. Would you like me to share the details?

🧩 Requirements
Python 3.9+

Streamlit

Ollama installed locally

faqs.json file containing Q&A pairs
