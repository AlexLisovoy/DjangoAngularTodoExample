# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if 'DJANGULAR_TODO_SECRET_KEY' not in os.environ:
    import random
    import string

    os.environ['DJANGULAR_TODO_SECRET_KEY'] = "".join([
        random.SystemRandom().choice(string.digits + string.ascii_letters +
                                     string.punctuation)
        for i in range(100)])
SECRET_KEY = os.environ['DJANGULAR_TODO_SECRET_KEY']

DEBUG = os.environ.get('DJANGULAR_TODO_DEBUG', True)

ALLOWED_HOSTS = [os.environ.get('DJANGULAR_TODO_ALLOWED_HOSTS', '127.0.0.1')]

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'rest_framework',
    'todo'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djangular_todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'djangular_todo', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangular_todo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
