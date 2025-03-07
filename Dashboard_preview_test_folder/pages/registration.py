import streamlit as st

st.set_page_config(page_title="Регистрация", layout="centered")

st.title("📝 Регистрация")

with st.form("registration_form"):
    st.text_input("Имя")
    st.text_input("Email")
    st.text_input("Пароль", type="password")
    submitted = st.form_submit_button("Зарегистрироваться")

st.page_link("Dashboard_login.py", label="🏠 Домой")
