import streamlit as st
if "user_id" not in st.session_state:
    st.switch_page("pages/0_Login.py")
from db import list_expenses
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Analytics")

# ✅ Get logged-in user
user_id = st.session_state["user_id"]

# ✅ Fetch only this user's expenses
rows = list_expenses(user_id)

if rows:
    df = pd.DataFrame(rows, columns=["ID", "Amount", "Category", "Note"])

    st.metric("Total Spent (₹)", f"{df['Amount'].sum():.2f}")

    by_cat = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(by_cat, labels=by_cat.index, autopct="%1.1f%%")
    ax.set_title("Spending by Category")

    st.pyplot(fig)
else:
    st.info("No expenses found for this user.")



