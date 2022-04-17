# My Car Reply Bot

Название бота - mycar_reply_bot. У него есть 2 команды - /start и /bind_token. Токен доступа будет в ответе при регистрации пользователя(access_token)

Основной адрес, на котором расположено API - https://tranquil-atoll-68970.herokuapp.com/

Для всех запросов необходимо добавить header Content-Type(application/json). Для запросов, требующих авторизации - Authorization(тип токена Bearer)

### Регистрация пользователя

POST /users/register/

Входящие параметры
- username:string
- password:string
- password_confirm:string 
- name:string

### Авторизация

POST /users/login/

Входящие параметры
- username:string
- password:string

### Отправка сообщений(требуется авторизация)

POST /messages/send/

Входящие параметры
- text:string

### Список отправленных сообщений(требуется авторизация)

GET /messages/list/


### Заключение

Не успел сделать некоторые вещи, т.к. был загруз по работе и я до этого не работал с heroku. Ниже перечислю что по плану
хотел еще сделать:
- Вынести отправку сообщений в celery задачу
- Изменить структуру - весь код вынести в отдельную папку(apps или src), в корневой папке оставить только настройки, 
  CI/CD файлы, requirements и т.д.
- Можно было бы добавить функцию для перегенерации токена доступа
- Если бы это был production проект, то токены доступа лучше было бы вынести в отдельные сущности с контролем их 
  активности, времени создания и т.д.