import environ

from sistemFusion.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', default=False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATASES = {
    'default': env.db(),
}