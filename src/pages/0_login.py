import streamlit as st
from db import login_user, register_user, init_db

init_db()

st.set_page_config(page_title="Login", layout="centered")

st.title("🔐 Login")

choice = st.radio("Choose", ["Login", "Register"])

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if choice == "Login":
    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state["logged_in"] = True
            st.session_state["user_id"] = user[0]
            st.session_state["username"] = username
            st.success("Logged in successfully")
            st.switch_page("app.py")

        else:
            st.error("Invalid credentials")

else:
    if st.button("Register"):
        try:
            register_user(username, password)
            st.success("Registered successfully! Now login.")
        except:
            st.error("Username already exists")
