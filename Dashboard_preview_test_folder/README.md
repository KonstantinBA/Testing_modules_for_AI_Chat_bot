# Dashboard Preview Test
![Image](https://github.com/KonstantinBA/Testing_modules_for_AI_Chat_bot/raw/main/Dashboard_preview_test_folder/image.png)
![Image](https://github.com/KonstantinBA/Testing_modules_for_AI_Chat_bot/raw/main/Dashboard_preview_test_folder/image1.png)
## 📌 Описание
Этот проект представляет собой **Streamlit Dashboard**, который содержит:
- Информацию о предстоящих мероприятиях (будет добавлено позже)
- Задачи по ближайшему мероприятию (будет добавлено позже)
- Маленький виджет погоды (будет добавлено позже)
- Окно для голосового/текстового чата с ИИ (будет добавлено позже)
- Боковую панель с навигацией (кнопки "Регистрация" и "Домой")

## 📁 Структура проекта
```
Dashboard_preview_test_folder/
│── Dashboard_login.py        # Главный файл (основной дашборд)
│── pages/
│   └── registration.py       # Страница регистрации
```

## 🚀 Запуск проекта
1. Установите **Streamlit**, если не установлен:
   ```sh
   pip install streamlit
   ```
2. Перейдите в папку с проектом и запустите Streamlit:
   ```sh
   streamlit run Dashboard_login.py
   ```

## 🔄 Навигация
- **Главная страница**: `Dashboard_login.py`
- **Страница регистрации**: `pages/registration.py`
- **Кнопка "Регистрация"** в боковой панели ведет на страницу регистрации.
- **Кнопка "Домой"** возвращает на главную страницу.

