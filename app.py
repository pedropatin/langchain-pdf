from dotenv import load_dotenv
import openai
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Consultant")
    st.header("Ask your PDF")

    # Upload file
    pdf = st.file_uploader("Upload your PDF" , type="pdf")

    # Extract content 
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 1000,
            chunk_overlap=200,
            length_function=len
        )
        
        chunks = text_splitter.split_text(text)

        # Create embeddings (vector representation of a piece of text)
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Show user question
        user_question = st.text_input("Ask a question about this document:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            st.write(docs)



    
if __name__ == '__main__':
    main()