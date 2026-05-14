from .base import *  # noqa

DEBUG = False

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
