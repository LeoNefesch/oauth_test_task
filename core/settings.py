import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = (os.getenv('DEBUG', 'false').lower() == 'true')

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
SOCIAL_APP_SECRET = os.getenv('SOCIAL_APP_SECRET')

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "users" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

ENGINE = 'django.db.backends.postgresql_psycopg2'

DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'OPTIONS': {'options': '-c search_path=sch_testdb,public'},
        'NAME': os.getenv('PG_DATABASE_TEST'),
        'USER': os.getenv('PG_USER_TEST'),
        'PASSWORD': os.getenv('PG_PASSWORD_TEST'),
        'HOST': os.getenv('PG_HOST_TEST'),
        'PORT': os.getenv('PG_PORT_TEST'),
        'DISABLE_SERVER_SIDE_CURSORS': True},
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
            'prompt': 'select_account',
        },
        'APP': {  # 'SocialAppName': 'Web client 1'
            'client_id': GOOGLE_CLIENT_ID,
            'secret': SOCIAL_APP_SECRET,
            'key': ''
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

LOGIN_URL = '/accounts/'
LOGIN_REDIRECT_URL = '/api/profile/'
LOGOUT_REDIRECT_URL = '/accounts/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
