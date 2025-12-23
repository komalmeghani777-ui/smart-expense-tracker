import streamlit as st
if "user_id" not in st.session_state:
    st.switch_page("0_Login.py")

from db import list_expenses, update_expense, delete_expense

st.title("📘 Expense History")

user_id = st.session_state["user_id"]

rows = list_expenses(user_id)

if rows:
    for exp_id, amt, cat, note in rows:
        with st.expander(f"#{exp_id} — ₹{amt}"):
            new_amt = st.number_input(
                "Amount", value=amt, key=f"amt_{exp_id}"
            )
            new_cat = st.text_input(
                "Category", value=cat, key=f"cat_{exp_id}"
            )
            new_note = st.text_area(
                "Note", value=note, key=f"note_{exp_id}"
            )

            if st.button("Update", key=f"upd_{exp_id}"):
                update_expense(
                    exp_id,
                    user_id,
                    new_amt,
                    new_cat.strip(),
                    new_note.strip()
                )
                st.success("Expense updated")
                st.rerun()

            if st.button("Delete", key=f"del_{exp_id}"):
                delete_expense(exp_id, user_id)
                st.error("Expense deleted")
                st.rerun()
else:
    st.info("No expenses found.")


