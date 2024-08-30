#Запуск приложения

export FLASK_APP=app.py     # На Windows: set FLASK_APP=app.py

flask run



#Тестирование API с помощью cURL
#1. Создание нового пользователя  
curl http://127.0.0.1:5000/users -X POST -H "Content-Type: application/json" -d '{"username": "user1"}'

#2. Создание ID пользователя 
curl http://127.0.0.1:5000/users -X GET -H "Content-Type: application/json" -d '{"id": 1, "username": "user1"}'


#3. Получение списка пользователй
curl http://127.0.0.1:5000/users/1 -X GET -H "Content-Type: application/json" -d '{"username": "user1"}'


#4. Создание нового поста
curl http://127.0.0.1:5000/posts/1 -X POST -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content", "author": {"id": 1, "username": "user1"}}'

#5.Редактирование поста
curl http://127.0.0.1:5000/posts -X PUT -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content editing", "author": {"id": 1, "username": "user1"}}'

#6.Удаление поста
curl http://127.0.0.1:5000/posts/1 -X DELETE -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content editing", "author": {"id": 1, "username": "user1"}}'


#Пример исполнения команд с выводом
# 1. Создание нового пользователя
curl http://127.0.0.1:5000/users -X POST -H "Content-Type: application/json" -d '{"username": "user1"}'

# 2. Получение списка всех пользователей
$ curl http://127.0.0.1:5000/users
[{"id": 1, "username": "user1"}]

# 3. Создание нового поста
$ curl http://127.0.0.1:5000/posts -X POST -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content", "author": {"id": 1, "username": "user1"}}'
{"id": 1, "title": "My First Post", "content": "This is the content", "author": "user1"}

# 4. Получение списка всех постов
$ curl http://127.0.0.1:5000/posts
[{"id": 1, "title": "My First Post", "content": "This is the content", "author": "user1"}]

# 5. Получение поста по ID
$ curl http://127.0.0.1:5000/posts/1
{"id": 1, "title": "My First Post", "content": "This is the content", "author": "user1"}

# 6. Обновление поста по ID
$ curl http://127.0.0.1:5000/posts/1 -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Post Title", "content": "Updated content"}'
{"id": 1, "title": "Updated Post Title", "content": "Updated content", "author": "user1"}

# 7. Удаление поста по ID
$ curl http://127.0.0.1:5000/posts/1 -X DELETE
{"message": "Post deleted successfully"}
