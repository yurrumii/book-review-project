Сайт с книгами
Добавление книг(автор, название и рейтинг, краткое описание)
Добавление рецензий (рейтинг, отзыв)
Стильный красивый сайт, оформленный в минимализме
Установка:
1. 
2. Виртуальное окружение 
3. python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
4. Установка зависимостекй: 
pip install -r requirements.txt
5. Миграции:
python manage.py migrate
6. Создание суперпользовтеля:
python manage.py createsuperuser
7. Запуск:
python manage.py runserver
