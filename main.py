import streamlit as st 
import pyshorteners as pyst
import pyperclip

def copying():
    pyperclip.copy(short_url)

shortner = pyst.Shortener()

st.markdown("<h1 style='text-align: center;'>URL Shortener</h1>", unsafe_allow_html=True)

form = st.form("Name")
url = form.text_input("URL HERE")
s_btn = form.form_submit_button("Submit")

if s_btn:
    short_url = shortner.tinyurl.short(url)
    st.title("SHORTED URL")
    st.markdown(f"<h6>{short_url}</h6>", unsafe_allow_html=True)
    st.button("Copy", on_click=copying)