import streamlit as st
from difflib import SequenceMatcher
import ollama

# ------------------ FAQ DATA ------------------
FAQS = {
    "minimum balance": "The minimum balance required to maintain your account is $500.",
    "account opening": "You can open an account online or by visiting the nearest branch with valid ID proof.",
    "loan interest rate": "Our personal loan interest rate starts from 10.5% per annum."
}

def get_faq_answer(user_query):
    """Return FAQ answer if user query matches closely."""
    user_query_lower = user_query.lower()

    # Exact match
    for question, answer in FAQS.items():
        if question in user_query_lower:
            return answer

    # Fuzzy match
    best_match = None
    highest_ratio = 0.0
    for question, answer in FAQS.items():
        ratio = SequenceMatcher(None, question, user_query_lower).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = answer

    # Only return if reasonably similar
    if highest_ratio > 0.6:
        return best_match
    return None

def query_ollama(user_query):
    """Query Ollama locally."""
    try:
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": user_query}])
        return response["message"]["content"]
    except Exception as e:
        return f"Error querying Ollama: {str(e)}"

# ------------------ STREAMLIT UI ------------------
st.set_page_config(page_title="Bank FAQ Chatbot", page_icon="💬")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "query" not in st.session_state:
    st.session_state.query = ""
if "last_question" not in st.session_state:
    st.session_state.last_question = ""
if "last_faq_answer" not in st.session_state:
    st.session_state.last_faq_answer = None

# Callback for sending a question
def ask_question():
    question = st.session_state.query.strip()
    if not question:
        return

    # Save last question
    st.session_state.last_question = question

    # Add user question to history
    st.session_state.history.append(("You", question))

    # Check FAQ first
    faq_answer = get_faq_answer(question)
    if faq_answer:
        st.session_state.history.append(("Bot (FAQ)", faq_answer))
        st.session_state.last_faq_answer = faq_answer
    else:
        # Fall back to Ollama
        ollama_answer = query_ollama(question)
        st.session_state.history.append(("Bot (Ollama)", ollama_answer))
        st.session_state.last_faq_answer = None

    # Clear the input field
    st.session_state.query = ""

# Callback for "Ask AI instead"
def ask_ai_instead():
    if not st.session_state.last_question:
        return
    ollama_answer = query_ollama(st.session_state.last_question)
    st.session_state.history.append(("Bot (Ollama)", ollama_answer))
    st.session_state.last_faq_answer = None

# Display history
st.markdown("## 💬 Smart Chatbot Partner")
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"**{sender}:** {message}")
    elif "(FAQ)" in sender:
        st.markdown(f"<span style='color:green;'>_{sender}:_ {message}</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color:blue;'>_{sender}:_ {message}</span>", unsafe_allow_html=True)

# Input and ask button
st.text_input("Type your question here:", key="query", on_change=ask_question)
st.button("Ask", on_click=ask_question)

# Show "Ask AI instead" button if FAQ answer was given
if st.session_state.last_faq_answer:
    st.info("Not satisfied with the FAQ answer?")
    st.button("🔍 Ask AI instead", on_click=ask_ai_instead)
