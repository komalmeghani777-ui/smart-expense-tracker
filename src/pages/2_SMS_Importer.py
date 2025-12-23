import streamlit as st
if "user_id" not in st.session_state:
    st.switch_page("0_Login.py")

import re

st.title("📩 SMS Importer")

sms_text = st.text_area("Paste SMS text here")

if st.button("Process SMS"):
    match = re.search(r'(?:Rs|INR)[\. ]?(\d+(?:\.\d+)?)', sms_text, re.IGNORECASE)

    if match:
        amt = float(match.group(1))

        # ✅ Store globally
        st.session_state["pending_amount"] = amt

        st.success(f"Amount detected: ₹{amt}")
        st.info("Go to Add Expense page to select category and save.")
    else:
        st.error("No amount detected.")


