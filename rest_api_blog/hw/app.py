import json
from flask import Flask, jsonify, request, abort
from hw.model.models import User, Post

app = Flask(__name__)

# Инициализация данных
users = []
posts = []

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'id': obj.id, 'username': obj.username}
        elif isinstance(obj, Post):
            return {'id': obj.id, 'title': obj.title, 'content': obj.content, 'author': obj.author.username}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder

# Маршрут для проверки связи
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})

# Пользователи
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data:
        abort(400)
    user = User(len(users) + 1, data['username'])
    users.append(user)
    return jsonify({'status': 'success', 'user': user}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        abort(404)
    return jsonify({'user': user})

# Посты
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data or 'author_id' not in data:
        abort(400)
    author = next((user for user in users if user.id == data['author_id']), None)
    if author is None:
        abort(404, description="Author not found")
    post = Post(len(posts) + 1, data['title'], data['content'], author)
    posts.append(post)
    return jsonify({'status': 'success', 'post': post}), 201

@app.route('/posts/<int:post_id>', methods=['GET'])
def read_post(post_id):
    post = next((post for post in posts if post.id == post_id), None)
    if post is None:
        abort(404)
    return jsonify({'post': post})

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post.id == post_id), None)
    if post is None:
        abort(404)
    data = request.get_json()
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    return jsonify({'status': 'success', 'post': post})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    post = next((post for post in posts if post.id == post_id), None)
    if post is None:
        abort(404)
    posts = [p for p in posts if p.id != post_id]
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
