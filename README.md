#Запуск приложения

export FLASK_APP=app.py     # На Windows: set FLASK_APP=app.py

flask run



#Тестирование API с помощью cURL

#1. Создание нового пользователя  
curl http://127.0.0.1:5000/users -X POST -H "Content-Type: application/json" -d '{"username": "user1"}'


#2. Получение списка пользователй
curl http://127.0.0.1:5000/users -X GET -H "Content-Type: application/json" -d '{"id": 1, "username": "user1"}'


#3. Создание ID пользователя 
curl http://127.0.0.1:5000/users/1 -X GET -H "Content-Type: application/json" -d '{"username": "user1"}'


#4. Создание нового поста
curl http://127.0.0.1:5000/posts -X POST -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content", "author": {"id": 1, "username": "user1"}}'


#5.Получение списка поста
curl http://127.0.0.1:5000/posts/1 -X GET -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content", "author": {"id": 1, "username": "user1"}}'


#6.Редактирование поста
curl http://127.0.0.1:5000/posts -X PUT -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content editing", "author": {"id": 1, "username": "user1"}}'


#7.Удаление поста
curl http://127.0.0.1:5000/posts/1 -X DELETE -H "Content-Type: application/json" -d '{"id": 1, "title": "My First Post", "content": "This is the content editing", "author": {"id": 1, "username": "user1"}}'
