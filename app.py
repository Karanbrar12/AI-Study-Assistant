import streamlit as st
from ingest import ingest_pdf
from chat import ask_ai

st.set_page_config(page_title="AI Study Assistant")

st.title("AI Study Assistant")

st.markdown("""
Upload a PDF and ask questions about your study material.

Features:
- Ask questions
- Generate summaries
- Create quizzes
- Generate flashcards
""")
audio=st.audio_input("Please say your query")
with st.sidebar:

    st.header("Settings")

    uploaded_file = st.file_uploader("Upload Study PDF", type="pdf")
    
    mode = st.selectbox(
        "Study Tool",
        ["Ask Question", "Summary", "Quiz", "Flashcards"]
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    ingest_pdf("temp.pdf")

    st.success("PDF successfully indexed")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

query = st.chat_input("Ask about your study material")

if query:

    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    if mode == "Summary":
        tool = "summary"
    elif mode == "Quiz":
        tool = "quiz"
    elif mode == "Flashcards":
        tool = "flashcards"
    else:
        tool = "ask"

    with st.spinner("Generating response"):
        result = ask_ai(query, tool)

    st.session_state.messages.append({"role": "assistant", "content": result})

    with st.chat_message("assistant"):
        st.write(result)