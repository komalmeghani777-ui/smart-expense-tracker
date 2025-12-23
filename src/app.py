import streamlit as st

# 🔐 If not logged in, go to Login page
if "user_id" not in st.session_state:
    st.switch_page("pages/0_Login.py")

st.set_page_config(
    page_title="Smart Expense Tracker",
    layout="centered"
)

# 📌 Sidebar
with st.sidebar:
    st.markdown("### 👤 Account")
    st.write(f"Logged in as **{st.session_state.get('username')}**")

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("0_Login.py")


st.title("Finexa Ledger by IoTrenetics Solutions Pvt. Ltd.")
st.write("Use the sidebar to navigate through the app.")

