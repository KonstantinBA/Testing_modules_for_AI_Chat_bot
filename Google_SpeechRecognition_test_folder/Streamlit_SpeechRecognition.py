import streamlit as st
import speech_recognition as sr
import os
import tempfile

def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Речь не распознана"
    except sr.RequestError:
        return "Ошибка сервиса распознавания"

st.title("Распознавание речи в текст")

st.markdown("""
### Инструкция:
1. Начните записывать голосовое сообщение, используя встроенную функцию Streamlit.
2. Остановите запись, когда будет необходимо.
3. Аудио будет обработано и преобразовано в текст.
""")

# Виджет для записи звука
audio_input = st.audio_input("Запишите голосовое сообщение")

if audio_input is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_input.read())
        temp_audio_path = temp_audio.name
    
    recognized_text = recognize_speech(temp_audio_path)
    st.text_area("Распознанный текст:", recognized_text)
    os.remove(temp_audio_path)
