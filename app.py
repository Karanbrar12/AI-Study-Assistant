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

with st.sidebar:

    st.header("Settings")

    uploaded_files = st.file_uploader(
    "Upload Study PDFs",
    type="pdf",
    accept_multiple_files=True
    )
    
    mode = st.selectbox(
        "Study Tool",
        ["Ask Question", "Summary", "Quiz", "Flashcards"]
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.indexed_file=None
        st.rerun()
if "index_file" not in st.session_state:
    st.session_state.indexed_file=None
if uploaded_files:

    for uploaded_file in uploaded_files:

        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.read())

        ingest_pdf(uploaded_file.name)

    st.success(f"{len(uploaded_files)} PDF(s) indexed successfully.")
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