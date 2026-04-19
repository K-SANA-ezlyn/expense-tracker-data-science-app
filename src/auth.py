import streamlit as st

def login():
    st.sidebar.title("Login System")

    # Initialize login state safely
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username.strip() == "admin" and password.strip() == "admin":
            st.session_state["logged_in"] = True
            st.sidebar.success("Login successful")
        else:
            st.session_state["logged_in"] = False
            st.sidebar.error("Invalid username or password")


def check_login():
    return st.session_state.get("logged_in", False)
