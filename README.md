# Привет, сегодня мы будем делать свой «Кинопоиск» с кучей разных фильмов!
### Эта курсовая потребует знания Flask, SQLAlchemy, Marshmallow, REST, CRUD, JWT и, конечно же, знаний и умений правильного создания структуры проекта.

## Описание проекта
- Установка зависимостей
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Создание моделей (очистит БД и создаст все модели, указанные в импорте)
```shell
python create_tables.py
```

- Загрузка данных в базу
```shell
python load_fixture.py
```
Скрпит читает файл fixtures.json и загружает данные в базу. Если данные уже загружены - выводит соответсвующее сообщение. 

## Запуск проекта

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run
```

### CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run
```

## Запуск тестов
```shell
pytest .
```


- **Аутентификация**
    
    Для того чтобы у каждого пользователя была возможность добавлять понравившиеся фильмы в закладки для просмотра позже, нам нужно их как-то разграничивать, поэтому мы организуем страницы с регистрацией и аутентификацией на основе уже изученной спецификации JWT.
    
- **Пользователи**
    
    У каждого пользователя будет страница с его профилем, где он сможет выбрать любимый жанр, указать имя и фамилию, а также в случае необходимости сменить пароль.
    
    Еще для пользователя нужно реализовать механизм добавления и удаления фильмов в/из закладок, а также просмотр всех сохраненных в закладки фильмов.
    
- **Фильмы, режиссеры, жанры**
    
    Конечно же, нужно добавить самые главные сущности — фильмы, режиссеры и жанры. Для них сделаем лишь возможность чтения (get-запросы).
    
    Для всех объектов будет работать пагинация, чтобы мы могли постранично выводить их на экран, а также можно будет посмотреть самые новые фильмы.


# Демонстрационный Frontend стенд
## Запуск из docker

1. Скачать и установить [docker](https://docs.docker.com/engine/install/)
2. Скачать образ командой `docker pull painassasin/node_cource_project:latest`
3. Запустить контейнер на 80 порту `docker run -p 80:80 painassasin/node_cource_project`

>Образ сконфигурирован таким образом, что он будет ожидать 
> backend на 5000 локальном порту
 
>Чтобы все корректно работало, нам нужно в проект установить еще один пакет
```python

from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from config import Config
from setup_db import db

api = Api(doc='/docs')


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config(Config))

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)
```

