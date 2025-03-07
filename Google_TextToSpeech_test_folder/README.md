# Преобразование текста в речь
![Image](https://github.com/KonstantinBA/Testing_modules_for_AI_Chat_bot/raw/main/Google_TextToSpeech_test_folder/image.png)
Простое веб-приложение на Streamlit, которое преобразует введённый текст в речь с помощью Google Text-to-Speech (gTTS).

## Установка и запуск

### Требования
- Python 3.7+
- Streamlit
- gTTS

### Установка зависимостей

```bash
pip install streamlit gTTS
```

### Запуск приложения

```bash
streamlit run Streamlit_TextToSpeech.py
```

## Использование
1. Введите текст в текстовое поле.
2. Нажмите кнопку "Преобразовать в речь".
3. Приложение сгенерирует аудиофайл и воспроизведёт его.

## Функционал
- Поддержка русского языка (можно изменить язык в коде `gTTS`).
- Генерация аудиофайла во временном хранилище.
- Автоматическое удаление временного файла после воспроизведения.

## Заметки
- Приложение использует `gTTS`, который требует подключения к интернету.
- Поддерживаемые языки можно посмотреть в документации `gTTS`.
