from .base import *

DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# EMAIL CONFIG
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False  # Use EMAIL_PORT 587 for TLS
DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
