import streamlit as st
from groq import Groq

# Ввод API-ключа пользователем (можно заменить на использование переменных окружения)
st.sidebar.title("Настройки")
api_key = st.sidebar.text_input("Введите ваш Groq API-ключ", type="password")

if not api_key:
    st.warning("Введите API-ключ для продолжения.")
    st.stop()

# Функция для работы с Groq API
def chat_with_ai(user_id, message):
    client = Groq(api_key=api_key)
    user_session = f"session_{user_id}"
    
    if user_session not in st.session_state:
        st.session_state[user_session] = []

    st.session_state[user_session].append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state[user_session],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    st.session_state[user_session].append({"role": "assistant", "content": response})
    return response

# Интерфейс Streamlit
st.title("AI Чат с Groq API")

# Разделение пользователей по сеансам
user_id = st.text_input("Введите ваше имя или ID пользователя", key="user_id")
if not user_id:
    st.warning("Введите имя, чтобы начать чат.")
    st.stop()

st.subheader(f"Чат для {user_id}")

# Поле ввода сообщения
user_input = st.text_input("Введите ваше сообщение:", key="user_input")

if st.button("Отправить") and user_input:
    response = chat_with_ai(user_id, user_input)
    st.text_area("Ответ от AI:", response, height=150)

# Отображение истории диалога
if f"session_{user_id}" in st.session_state:
    st.subheader("История чата")
    for msg in st.session_state[f"session_{user_id}"]:
        role = "🤖 AI" if msg["role"] == "assistant" else "🧑‍💻 Вы"
        st.markdown(f"**{role}:** {msg['content']}")
