import streamlit as st
if "user_id" not in st.session_state:
    st.switch_page("pages/0_Login.py")
from db import add_expense

st.title("➕ Add Expense")

user_id = st.session_state["user_id"]

# ✅ Initialize once
if "pending_amount" not in st.session_state:
    st.session_state["pending_amount"] = 0.0

amount = st.number_input(
    "Amount (₹)",
    value=float(st.session_state["pending_amount"]),
    step=1.0
)

category = st.text_input("Category (Food, Travel, etc.)")
note = st.text_area("Note")

if st.button("Save Expense"):
    if not category.strip():
        st.error("Please enter a category.")
    else:
        add_expense(
            user_id,
            amount,
            category.strip(),
            note.strip()
        )

        # ✅ Clear AFTER saving
        st.session_state["pending_amount"] = 0.0

        st.success("Expense saved successfully ✅")

