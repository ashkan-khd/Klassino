import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from karino.settings.development import *

DEBUG = False

# allowed hosts

ALLOWED_HOSTS = [
    'karen-edu.ir',
    'www.karen-edu.ir',
    'api.karen-edu.ir',
    '37.152.176.13'
]

CORS_ORIGIN_WHITELIST = [
    "http://www.karen-edu.ir",
    "https://www.karen-edu.ir",
    "http://karen-edu.ir",
    "https://karen-edu.ir",
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
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5435',
    }
}

# caching

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6380/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# statsd

STATSD_HOST = 'karino_graphite'
STATSD_PORT = 8125
STATSD_PREFIX = 'karino_api'

# cronjobs

CRONJOBS = [
]

# sentry

# sentry_sdk.init(
#     dsn="https://fcc373b13a8e4d34a3e090c17f1088ec@o402116.ingest.sentry.io/5262683",
#     integrations=[DjangoIntegration()],
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )
