# Notes API (FastAPI + SQLite)

Простий REST API для нотаток у форматі Markdown.  
Зроблено на **FastAPI** з використанням **SQLite** як бази даних.

## 🚀 Можливості
- Створення нотаток з тегами
- Отримання нотатки з конвертацією Markdown → HTML
- Видалення нотаток
- Пошук нотаток за тегами
- Swagger UI для тестування (`/docs`)

## 📂 Структура
notes_api/
├── main.py          # FastAPI застосунок
├── notes.db         # SQLite база (створюється автоматично)
├── requirements.txt # Залежності

## ⚙️ Встановлення
```bash
git clone https://github.com/hornymothvt-debug/notes-api.git
cd notes-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
