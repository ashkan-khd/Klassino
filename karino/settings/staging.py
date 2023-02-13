import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from karino.settings.development import *

DEBUG = False

# allowed hosts

ALLOWED_HOSTS = [
    'staging.api.karino.ir',
    'staging.karino.ir',
]

CORS_ORIGIN_WHITELIST = [
    "https://staging.karino.ir",
]

# logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{asctime} {name} {levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'karino',
        'USER': 'karino',
        'PASSWORD': 'karino',
        'HOST': 'karino_db_staging',
        'PORT': '5432',
    }
}

# caching

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://karino_cache_staging:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
