import streamlit as st 
from PyPDF2 import PdfReader
from utils import text

def main():
    st.set_page_config(page_title = 'pergunte aos seus arquivos'page_icon=books:)
    
    with st.siderbar:
        st.subheader('seus arquivos')
        pdf_docs = st.file_uplouder("carregue seus arquivos em formato pdf"accept_multiple_files=True)
        print(pdf_docs)
        if st.buttons('Processar'):
            all_files_text = text.process_files(pdf_docs)
            chunks = text.create_text_chunks(all files text)
if_name_ =='_main_':
    main() 
