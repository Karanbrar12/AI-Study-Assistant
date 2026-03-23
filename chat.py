import warnings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core._api.deprecation import LangChainDeprecationWarning
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
warnings.filterwarnings("ignore",category=LangChainDeprecationWarning)
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb=Chroma(persist_directory="BOT_DB",
                embedding_function=embeddings)

chat_history=""
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",  
    google_api_key="API_KEY",
    temperature=0.3,
)
def ask_ai(query, mode="ask"):

    docs=vectordb.similarity_search(query,k=2)
    context="\n\n".join([doc.page_content for doc in docs])

    if mode=="summary":

        prompt=f"""
        Summarize the following study material clearly for students.

        {context}
        """

    elif mode=="quiz":

        prompt=f"""
        Create 5 quiz questions from this study material.

        {context}
        """

    elif mode=="flashcards":

        prompt=f"""
        Create flashcards from this study material.

        Format:
        Question:
        Answer:

        {context}
        """

    else:

        prompt=f"""
        Answer the student's question using this context.

        Context:
        {context}

        Question:
        {query}
        """

    response = llm.invoke(prompt)
    return response.content