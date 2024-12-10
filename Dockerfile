# Базовый образ Python
FROM python:3.11-slim

# Установите зависимости
RUN apt-get update && apt-get install -y gcc g++ libffi-dev libssl-dev netcat-openbsd

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

RUN chmod +x startup.sh
# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.dev.txt

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Команда для выполнения миграций, создания пользователей и запуска сервера

CMD ["sh", "/app/startup.sh"]