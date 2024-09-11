from django.conf import settings

# App-specific CORS settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Replace with your frontend's origin
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
]

CORS_ALLOW_HEADERS = [
    'Authorization',
    'Content-Type',
]