# test-task-for-kokoc
Сервис для прохождения опросов пользователями. На сайте доступна регистрация.
За прохождение тестов пользователь получает монеты , за которые можно поменять
цвет логина. Лучшие попадают в список на отдельной странице.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ravimb06/test-task-for-kokoc.git
```

```
cd test-task-for-kokoc
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
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

### Использованные технологии:
- Python 3
- Django

## Автор
**[Али Богатырев](https://github.com/ravimb06)**
