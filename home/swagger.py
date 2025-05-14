from drf_yasg import openapi

swagger_tags = [
    {
        'name': 'authentication',
        'description': 'JWT Authentication endpoints'
    },
    {
        'name': 'todos',
        'description': 'CRUD operations for Todo items'
    }
]

security_definitions = {
    "Bearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "JWT authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
    }
}