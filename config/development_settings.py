from .base_settings import *

DEBUG = False
INTERNAL_IPS.append('46.101.243.200')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/static/'
STATIC_ROOT = '/vol/web/static'
MEDIA_URL = '/static/media/'
MEDIA_ROOT = '/vol/web/media'
