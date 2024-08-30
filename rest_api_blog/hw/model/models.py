class User:
    def __init__(self, user_id, username: str):
        self.username = username
        self.id = user_id

class Post:
    def __init__(self, post_id, title, content, author):
        self.id = post_id
        self.title = title
        self.content = content
        self.author = author
