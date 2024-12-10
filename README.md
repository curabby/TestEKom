Проект Django с MongoDB для выполнения Тестового задания компании е.Ком

Описание проекта
Этот проект разработан на Django с использованием MongoDB в качестве базы данных. Предназначен для демонстрации функционала Django-приложения, включая тестовые данные и авторизацию через суперпользователя.

Требования
Перед началом убедитесь, что у вас установлены:

Docker (для запуска контейнеров).
Docker Compose (для управления сервисами).
Python (если не используете Docker).


Развёртывание и запуск проекта
Шаг 1: Клонируйте репозиторий
git clone https://github.com/curabby/TestEKom.git
cd TestEKom

Шаг 2: Запустите контейнеры
Используйте Docker Compose для запуска проекта:
docker-compose up --build -d

Шаг 3: Ожидайте инициализации
При первом запуске контейнер выполнит следующие действия:

Выполнит миграции базы данных.
Добавит тестовые данные.
Создаст суперпользователя.

Доступ к приложению
1. Вход в админ-панель
Админ-панель доступна по адресу:
http://localhost:8000/admin/

Используйте следующие данные для входа:
Email: super-user@mail.com
Пароль: 1234SuperUser*

Тестовые данные
При первом запуске автоматически добавляются тестовые записи:

Пользователи: 7 тестовых пользователей, 1 суперпользователь.
Шаблоны: 20 тестовых шаблонов.
Используйте их для проверки работы приложения.

К примеру через Postman можно направить пост запрос следующего вида передав соответсвующие параметры (не забудьте заменить на данные созданные в БД при развертке приложения)
POST http://localhost:8000/api/v1/get_form/?email=christinayoung@example.ru&phone_number='+7 801 188 23 59'

2. Документация API (Swagger)
Swagger-документация доступна по адресу:
http://localhost:8000/swagger/

Полезные команды
Остановить контейнеры
docker-compose down

Перезапустить проект
docker-compose up --build -d


