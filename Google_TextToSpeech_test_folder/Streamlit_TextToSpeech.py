import streamlit as st
from gtts import gTTS
import tempfile
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='ru', )  # Укажите язык, например, 'ru' для русского
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

st.title("Преобразование текста в речь")

# Поле для ввода текста
text = st.text_area("Введите текст:")

if st.button("Преобразовать в речь"):
    if text.strip():
        audio_file = text_to_speech(text)
        st.audio(audio_file, format='audio/mp3')
        
        # Удаление временного файла после завершения
        os.remove(audio_file)
    else:
        st.warning("Введите текст для преобразования!")