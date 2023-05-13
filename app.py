from dotenv import load_dotenv
import openai
import streamlit as st
from PyPDF2 import PdfReader
import os

def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Consultant")
    st.header("Ask your PDF")

    pdf = st.file_uploader("Upload your PDF" , type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader()

    
if __name__ == '__main__':
    main()