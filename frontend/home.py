import streamlit as st

def home():
    st.title("Welcome to the ERP Home Page")
    
    if 'user' in st.session_state:
        st.success("You are logged in.")
        st.write("Home page content goes here...")  # Customize your home page
    else:
        st.warning("Please log in to access this page.")

if __name__ == '_main_':
    home()