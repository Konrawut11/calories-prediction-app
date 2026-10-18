import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# เปิดและอ่านไฟล์ app.html
with open("app.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# แสดงผลบน Streamlit
components.html(html_content, height=900, scrolling=True)
