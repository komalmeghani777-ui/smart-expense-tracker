import streamlit as st

if "user_id" not in st.session_state:
    st.info("Please login to continue.")
    st.switch_page("0_Login.py")
    st.stop()


from PIL import Image
import pytesseract
import re
import os
user_id = st.session_state["user_id"]

st.title("🧾 Receipt OCR")

TES_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TES_PATH):
    pytesseract.pytesseract.tesseract_cmd = TES_PATH

uploaded = st.file_uploader("Upload receipt image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, use_column_width=True)

    text = pytesseract.image_to_string(img)
    st.text_area("Extracted Text", text)

    nums = re.findall(r'\d+\.\d+|\d+', text)
    nums = [float(n) for n in nums]

    if nums:
        chosen = st.selectbox("Detected amounts", nums)
        if st.button("Use this amount"):
            st.session_state["pending_amount"] = chosen
            st.success(f"Amount set to ₹{chosen}")
            st.info("Go to Add Expense to save it.")
    else:
        st.warning("No amount detected.")
