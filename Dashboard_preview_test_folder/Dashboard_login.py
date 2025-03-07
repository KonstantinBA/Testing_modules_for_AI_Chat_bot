import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Dashboard", layout="wide")

# Боковая панель с кнопками
st.sidebar.title("Навигация")
if st.sidebar.button("Регистрация"):
    st.switch_page("registration")

# Основной заголовок
st.title("📊 Дашборд мероприятий")

# Создание колонок для сетки
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📅 Ближайшие мероприятия")
    st.info("🔹 Здесь будет информация о мероприятиях...")

    st.subheader("✅ Задачи по ближайшему мероприятию")
    st.warning("📌 Здесь будут задачи...")

with col2:
    st.subheader("⛅ Погода")
    st.success("🌤 Виджет погоды...")

    st.subheader("💬 Чат с ИИ")
    st.text_area("Чат с AI (будет реализован позже)", height=200)

