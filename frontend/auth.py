import streamlit as st
from backend.db import get_users_collection
from backend.utils import hash_password

# Signup functionality
def signup():
    st.title("Sign Up")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        if username and password:
            hashed_password = hash_password(password)
            
            users_collection = get_users_collection()
            
            if users_collection.find_one({"username": username}):
                st.warning("Username already exists!")
            else:
                users_collection.insert_one({"username": username, "password": hashed_password})
                st.success("Account created successfully! You can now log in.")
        else:
            st.warning("Please fill in all fields.")

# Login functionality
def login():
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username and password:
            hashed_password = hash_password(password)
            users_collection = get_users_collection()
            user = users_collection.find_one({"username": username, "password": hashed_password})
            
            if user:
                st.success("Logged in successfully!")
                st.session_state["user"] = user["_id"]
                st.experimental_set_query_params(page="home")  # Redirect-like behavior
            else:
                st.warning("Invalid username or password!")
        else:
            st.warning("Please fill in all fields.")

# Main function to display login or signup page
def main():
    query_params = st.experimental_get_query_params()
    if "user" not in st.session_state:
        st.sidebar.title("Welcome")
        choice = st.sidebar.radio("Choose an option", ["Login", "Sign Up"])

        if choice == "Login":
            login()
        else:
            signup()
    else:
        # Redirect-like behavior based on query params
        if query_params.get("page") == ["home"]:
            st.success("Welcome to the Home Page!")
            st.write("You are successfully logged in.")
        else:
            st.success("You are logged in!")
            st.write("Redirecting to home page...")

if __name__ == "_main_":
    main()