# Django Auth Service
A microservice that allows you to bootstrap a user management REST API, based on Django REST Framework with a JSON Web Token authentication backend included.

## Dependencies
- Django REST Registration - https://github.com/apragacz/django-rest-registration
- Simple JWT - https://github.com/davesque/django-rest-framework-simplejwt
- Django REST Swagger - https://github.com/marcgibbons/django-rest-swagger

## Installation
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Setup
### Essential setup

Please perform the following setup at `settings.py`:

**Specify hosts allowed to use the microservice**
```python
ALLOWED_HOSTS = ['127.0.0.1']
```

**Setup email service used for the login\registration\password reset workflows**

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'youremail@example.com'
EMAIL_HOST_PASSWORD = 'YourLeetPassword'
```

**Django REST Registration setup, please note that by default the verification workflows is disabled**

```python
REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': False,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
    'REGISTER_VERIFICATION_URL': 'https://frontend-host/verify-user/',
    'RESET_PASSWORD_VERIFICATION_URL': 'https://frontend-host/reset-password/',
    'REGISTER_EMAIL_VERIFICATION_URL': 'https://frontend-host/verify-email/',
    'VERIFICATION_FROM_EMAIL': 'no-reply@example.com',
}
```

**Setup CORS with by allowing all origins or whitelisting**
```python
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://1.1.1.1"
]
```

**Setup JSON Web Tokens backend**
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```

## (WIP) Examples of usage
**Register a user**

```bash
curl --request POST \
  --url http://localhost:8000/api/v1/accounts/register/ \
  --header 'content-type: application/json' \
  --data '{
	"username": "vlameiras",
	"email": "mail@example.com",
	"password": "mypass1",
	"password_confirm": "mypass1",
}'
```

**Request a valid JWT**
```bash
curl --request POST \
  --url http://localhost:8000/api/v1/accounts/token/ \
  --header 'content-type: application/json' \
  --data '{
	"username": "vlameiras",
	"password": "mypass1"
}
```

**Logout**
```bash
curl --request POST \
  --url http://localhost:8000/api/v1/accounts/logout/ \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxMDA3MjAzLCJqdGkiOiI4NjgzYjFkYTg0YmY0OWE1YWZmOTg4MWU2YjIxZmIwNiIsInVzZXJfaWQiOjN9.isk6xYbsF2GpgZ1Hb64afK_QX8x-hM_zb7x4tXukzEA' \
  --header 'content-type: application/json' \
  --data '{
	"username": "vlameiras",
	"password": "mypass1"
}'
``` 

## Documentation
- https://django-rest-registration.readthedocs.io/en/latest/
- https://github.com/davesque/django-rest-framework-simplejwt

## Notes
Django REST Swagger has been deprecated a replacement suggestion to be considered is https://github.com/axnsan12/drf-yasg