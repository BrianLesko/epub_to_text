##################################################
# About the author: Brian Lesko is a robotics engineer and recent graduate
# This code implements some some gui shortcuts that are used to customize the app.py file, mainly using the low code streamlit library.

import streamlit as st

# Version 1.0.0

class gui():
    def __init__(self):
        pass
    def about(self, photo = 'docs/bl.png', author = "Brian", text = "In this code we ... "):
        with st.sidebar:
            col1, col2, = st.columns([1,5], gap="medium")
            with col1:
                st.image(photo)
            with col2:
                st.write(f""" 
                Hey it's {author}, \n
                {text}
                """)
            col1, col2, col3, col4, col5, col6 = st.columns([1.1,1,1,1,1,1.5], gap="medium")
            with col2: # Twitter
                st.write("[![X](https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-335095-blue/x-logo-blue.svg)](https://twitter.com/BrianJosephLeko)")
            with col3: # GITHUB
                st.write("[![Github](https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-335095-blue/github-mark-blue.svg)](https://github.com/BrianLesko)")
            with col4: # LINKEDIN
                st.write("[![LinkedIn](https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-335095-blue/linkedin-icon-blue.svg)](https://www.linkedin.com/in/brianlesko/)")
            with col5: # YOUTUBE
                "." #st.write("[![LinkedIn](https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-335095-blue/yt-logo-blue.svg)](https://www.linkedin.com/in/brianlesko/)")
            with col6: # BLOG Visual Study Code
                "." #"[![VSC]()](https://www.visualstudycode.com/)"

    def clean_format(self):
        hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
                </style>
                """
        st.markdown(hide_st_style, unsafe_allow_html=True)

    def display_existing_messages(self,intro = "Type in the chat box to embed some text"):
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": intro}]
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    def input_api_key(self):
        st.write('  ') 
        st.markdown("""---""")
        if not openai_api_key:
            openai_api_key = st.text_input("# OpenAI API Key", key="chatbot_api_key", type="password")
            col1, col2 = st.columns([1,5], gap="medium")
            with col2:
                "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        return openai_api_key