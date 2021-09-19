EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'goodman@africaherbabank.org'
EMAIL_HOST_PASSWORD = 'vanjerry@81'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



RECAPTCHA_PUBLIC_KEY = "6LfOHrYbAAAAAFR8hGuSsSf9LKnoxOeHLgDn7MCF"
RECAPTCHA_PRIVATE_KEY = "6LfOHrYbAAAAAECNrzG1pBX7aaHH9cc5Ov6K1rXa"
NORECAPTCHA = True




SECRET_KEY = 'django-insecure-ra+!(a(@7xup0dftqpghtpn$k+piyq&nb#x223jrz_0s^qu25w'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['africaherbalbank.org', '*', '0.0.0.0', 'localhost', '162.213.253.39'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'