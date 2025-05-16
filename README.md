ToDo API - Django REST Framework with JWT Authentication & Swagger Documentation
A full-featured Django REST Framework (DRF) ToDo application that includes JWT (JSON Web Token) authentication and Swagger documentation for easier development and testing.

🚀 Features
Task Management: Create, update, get, put, patch, and delete, search,  tasks.

Token-based Authentication: Secure login and session management using JWT.

Interactive API Documentation: Automatically generated Swagger UI docs to visualize and test the API.

DRF Best Practices: Follows best practices for building REST APIs with Django and DRF.

📋 Setup Instructions
Prerequisites
Before setting up the project, make sure you have the following installed:

Python 3.13+

Django 4.x+

Django REST Framework (DRF)

SQLite (or other databases you prefer)

Installation Steps
Clone the Repository:

Open your terminal and run the following command to clone the project:

http://127.0.0.1:8000

git clone https://github.com/ashraf940/rest-framework-api.git
cd rest-framework-api
Install Dependencies:

Install the required Python packages:

t
pip install -r requirements.txt
Apply Database Migrations:

Set up your database by running the following command to apply migrations:


python manage.py migrate
Run the Development Server:

Start the Django development server:


python manage.py runserver
The application should now be running at http://localhost:8000.

🔑 Authentication API Endpoints
1. Register a New User
Method: POST

Endpoint: /api/auth/register/

Description: Register a new user by providing a username and password.

2. Login & Get JWT Tokens
Method: POST

Endpoint: /api/token/

Description: Login with your username and password to receive an access token and refresh token.

Request Body Example:


{
  "username": "admin",
  "password": "asd"
}
3. Refresh JWT Token
Method: POST

Endpoint: /api/token/refresh/

Description: Refresh an expired JWT access token using the refresh token.

4. Get User Profile
Method: GET

Endpoint: /api/auth/profile/

Description: Retrieve the profile information of the currently authenticated user. Requires JWT token in the request header.

📝 Task Management API Endpoints
1. Get All Tasks
Method: GET

Endpoint: /api/todo/

Description: Get all tasks. Requires authentication (JWT).

2. Create a New Task
Method: POST

Endpoint: /api/todo/

Description: Create a new task. Requires authentication (JWT).

Request Body Example:

json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
3. Update a Task
Method: PUT

Endpoint: /api/todo/{id}/

Description: Update an existing task. Requires authentication (JWT).

4. Delete a Task
Method: DELETE

Endpoint: /api/todo/{id}/

Description: Delete a specific task by ID. Requires authentication (JWT).

📚 API Documentation
Swagger UI
The API documentation is automatically generated and can be accessed at:

Swagger UI Documentation

🔐 Authentication Flow
Register: Use /api/auth/register/ to create a new user.

Login: Use /api/token/ to get the JWT tokens.

Access Protected Endpoints: Use the JWT access token for authentication in subsequent API requests.

Refresh Tokens: Use /api/token/refresh/ to refresh expired tokens.

Authentication Header Example
plaintext

Authorization: Bearer <your_access_token>
🛠️ Development & Contribution
Running Tests
Make sure to run tests before pushing any changes:


python manage.py runserver
