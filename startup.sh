#!/bin/bash
echo "Ожидание подключения к MongoDB..."
while ! nc -z mongodb 27017; do
    sleep 1
done
echo "MongoDB готова."

echo "Выполняем миграции..."
python manage.py makemigrations
python manage.py migrate

echo "Заполняем базу данных..."
# Запускаем команду для создания 15 пользователей
python manage.py create_users
# Запускаем команду для создания 50 шаблонов
python manage.py create_templates
# Создаем суперпользователя через хендлер
python manage.py create_superuser

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем сервер
python manage.py runserver 0.0.0.0:8000