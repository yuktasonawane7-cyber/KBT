import streamlit as st

st.markdown("""
<style>
            

            .stButton>button
            {
            background-color:yellow;
            color:black;
            border-radius:10px;}
</style>









""",unsafe_allow_html=True)

st.title("Simple Registration Form")

with st.form("my_form"):

    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, step=1)
    email = st.text_input("Enter your email")

    submit = st.form_submit_button("Submit")


if submit:
    st.success("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Email:", email)




