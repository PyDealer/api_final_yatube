# api_final
### api final - это:
проект API блога yatube, с помощью которого можно:
просматривать, добавлять, удалять посты и комментарии,
а также подписываться на пользователей.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:PyDealer/api_final_yatube.git
```

```
cd api_final
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:
http://127.0.0.1:8000/api/v1/posts/

http://127.0.0.1:8000/api/v1/posts/{id}/

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

http://127.0.0.1:8000/api/v1/groups/

http://127.0.0.1:8000/api/v1/groups/{id}/

http://127.0.0.1:8000/api/v1/follow/

### Полную документацию к API можно посмотреть, предварительно запустив проект, по адресу:

```
http://127.0.0.1:8000/redoc/
```

### Аутентификация осуществляется с помощью токена JWT:
Для получения токена нужно создать пользователя через django:

```
python manage.py createsuperuser
```

Далее отправить post-запрос на эндпоинт http://127.0.0.1:8000/api/v1/follow/:

```
{
"username": "string",
"password": "string"
}
```
При валидных данных в ответ вернется 2 токена: "access" - для использования,
"refresh" - для обновления токена.

### Настройки на уровне проекта для токена:

```
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```
