from .base import *

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'    #for the pictures/images
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #for resetting my password
SYSTEM_EMAIL = 'admin@mysitename.com'