from decouple import config

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False  # Use EMAIL_PORT 587 for TLS
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
