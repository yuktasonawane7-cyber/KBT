import streamlit as st
st.title("simple chatbot")

Question=st.text_input("Ask ne anything")
if st.button("Start Chatting"):
    st.write("you asked:",Question)
    st.write("Chatbot is thinking...")