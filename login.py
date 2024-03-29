import streamlit as st
st.title("welcome to Digipodium institue")
Name=st.text_input('Your good name',type='default')
number=st.text_input('Your phone number',type='default')
fun=st.selectbox("Login or signup",['login','signup'])
if fun=='login':
    email=st.text_input('Email address')
    password=st.text_input('Password(at least 8 digit)',type='password')
    st.button('login')
else:
    email=st.text_input('Email address')
    password=st.text_input('at least 8 digit',type='password')