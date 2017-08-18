import os, sys
from os.path import abspath, join, dirname

CURRENT_DIR = abspath(join(dirname(__file__), '../', '../'))
sys.path.append(join(CURRENT_DIR, 'nymdesign'))
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CURRENT_DIR, 'test_setup', 'db2.sqlite3'),
    }
}

ADMINS = (('fname lname', 'email@email.com'),)

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(CURRENT_DIR, '../', 'static_media'),
)
STATIC_ROOT = os.path.join(CURRENT_DIR, '../', 'test_serve_static')



MEDIA_ROOT = os.path.join(CURRENT_DIR, '../', 'uploaded_media')
MEDIA_URL = 'http://127.0.0.1:8000/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '(c5%3igs862kyb3_su4e^!01zqr_b4-wd-1bte+rkw66+#kz8b'


ROOT_URLCONF = 'nymdesign.urls_test'

TEMPLATE_DIRS = (   os.path.join(CURRENT_DIR, 'nymdesign', 'templates'),
)

INSTALLED_APPS =  (
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'nymdesign.portfolio',
    #'nymdesign.working_papers',
    'nymdesign.info_pages',
)


ALLOWED_HOSTS =['localhost'\
	,'127.0.0.1'\
	]
