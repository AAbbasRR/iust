## Abrat Backend

env variables:

    # ___Project Setup___ #
    SECRET_KEY = string
    Debug_Status = bollean
    # __Redis Setup__ #
    Redis_Host = url[localhost]
    Redis_port = int
    Redis_db = int
    # ___Email Setup___ #
    EMAIL_HOST = email[mail.valmart.net]
    EMAIL_HOST_USER = email[vlmtest@mail.valmart.net]
    EMAIL_HOST_PASSWORD = string
    EMAIL_PORT = int
    EMAIL_USE_SSL = boolean
    DEFAULT_FROM_EMAIL = string


How To Run:

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver