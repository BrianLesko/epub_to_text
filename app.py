# Brian Lesko
# 11/24/2023

import os
import io
import zipfile
from bs4 import BeautifulSoup
import streamlit as st
from customize_gui import gui as gui 
gui = gui()

def extract_text_from_epub(file_stream):
    with zipfile.ZipFile(file_stream, 'r') as myzip:
        content = []
        for name in myzip.namelist():
            if name.endswith('.html') or name.endswith('.xhtml'):
                with myzip.open(name) as myfile:
                    soup = BeautifulSoup(myfile, 'html.parser')
                    content.append(soup.get_text())
        return '\n'.join(content)
    
gui.clean_format()
with st.sidebar:
    gui.about(text="This code implements Text extraction from an epub file.")

upload = st.file_uploader("Upload an ePub file", type="epub")

if upload:
    filename = upload.name
    st.subheader(f"Uploaded file: {filename}")
    with st.spinner("Extracting text from ePub file..."):
        
        # Converting the uploaded file to a byte stream
        file_stream = io.BytesIO(upload.getvalue())
        
        # Extracting text from the ePub file
        text = extract_text_from_epub(file_stream)
        
        # Displaying the extracted text
        st.subheader("Extracted Text")
        st.write(text)

        with st.sidebar:
            st.write('')
            "---"
            st.write('')
            col1, col2, col3 = st.columns([1,1,1])
            with col2: 
                st.download_button(
                    label="Download Text",
                    data=text,
                    file_name= filename + ".txt",
                    mime="text/plain",
                    )
            st.write('')
            "---"


