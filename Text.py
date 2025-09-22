from PyPDF2 import PdfReader
from langchain.text_splitter import CharacteresTextSplitter


def process_files(files):
    text = ""
    
    
    for file in files:
        pdf = PdfReader(file)
        for page in pdf.pages: 
            text +=page.extract_text()
        return text
        
    def create_text_chuncks(text):
        text_splitter = CharacteresTextSplitter(
            separatir = '\n'
            chuck_size = 1500,
            chuck_overlap = 300,
            length_fuction = len)
            
            chunks = text_splitter.split_text(text)
            return chunks
