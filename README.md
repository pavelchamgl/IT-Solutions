# Ads platform

Этот API представляет собой бэкенд для системы сбора данных о объявлениях.

## Запуск проекта

Чтобы запустить проект:

1. Клонируйте репозиторий: `git clone <repository_url>`
2. Перейдите в директорию проекта: `cd task_manager`
3. Создайте файл `.env` и заполните его переменными окружения, следуя примеру в `example.env`, если это необходимо.
4. Запустите проект с помощью: `python3 backend/manage.py runserver`

## Технические детали

### Основные используемые технологии

- **Django REST Framework**: Фреймворк для создания веб-API на основе Django.
- **SQLite3**: База данных, используемая для хранения данных приложения.
- **beautifulsoup4 и selenium**: Используется для парсинга данных.

## Документация API

После запуска проекта вы сможете найти документацию API по адресу [http://localhost:8000/schema/swagger/](http://localhost:8000/api/swagger/).

### Примечание

Проект поставляется с товой базой данных. Для входа в административную панель [http://localhost:8000/admin/](http://localhost:8000/api/swagger/) используйте следующие учетные данные:

- Email: admin@admin.com
- Пароль: admin

## Обзор конечных точек

### Управление объявлениями

- **GET /api/ads/**: Получение первых десяти объявлений .
- **GET /api/parse-ads/**: Список всех объявлений записаных в базу.
- **GET /api/ads/{ad_id}/**: Детальное отображение информации объявления.

Эти конечные точки предоставляют функционал для сбора и просмотра объявлений.

### Управление пользователями

- **POST /api/accounts/register/**: Регистрация нового пользователя.
- **POST /api/accounts/email/confirmation/**: Подтверждение адреса электронной почты пользователя.
- **POST /api/accounts/email/otp/resend/**: Повторная отправка OTP для подтверждения адреса электронной почты.
- **POST /api/accounts/login/**: Вход пользователя в систему с получением JWT токена.
- **POST /api/accounts/logout/**: Выход пользователя из системы и инвалидация токена.
- **POST /api/accounts/check-otp-password-reset/**: Проверка OTP для сброса пароля.
- **POST /api/accounts/password/reset/confirmation/**: Подтверждение сброса пароля.
- **GET /api/accounts/profile/me/**: Получение текущего профиля пользователя.
- **PUT /api/accounts/profile/update/**: Обновление профиля текущего пользователя.
- **POST /api/accounts/deletion/me/**: Запрос на удаление своей учетной записи.
- **POST /api/accounts/token/refresh/**: Обновление JWT токена.
- **POST /api/accounts/password/reset/otp/send/**: Отправка OTP для сброса пароля.


Эти конечные точки предоставляют функционал для управления пользователями включая регистрацию, аутентификацию, управление профилями, а также управление сеансами и сброс паролей.