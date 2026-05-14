from .base import *  # noqa

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
