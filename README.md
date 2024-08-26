Instructions for Integrating and Using This Model in a Web Service
1. Setup:
Ensure that the file models.py is in your project directory.
This file defines the models for User and Post.

2. HTTP Endpoints:
Below are example HTTP methods and URLs for interacting with these models in a REST API context.

Create a New User
URL: /users
Method: POST
Request Body:
{
    "user_id": 1,
    "username": "john_doe"
}

Description: This will create a new user with the given user_id and username.

Create a New Post
URL: /posts
Method: POST
Request Body:
{
    "post_id": 1,
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "author": 1
}
Description: This will create a new post associated with the user whose id is 1.


Retrieve All Users
URL: /users
Method: GET
Description: This will return a list of all users.

Retrieve All Posts
URL: /posts
Method: GET
Description: This will return a list of all posts.

