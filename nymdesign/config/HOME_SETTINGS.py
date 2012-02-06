import os
import sys

CURRENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../'))
sys.path.append(os.path.join(CURRENT_DIR, 'nymdesign'))

DEBUG = True

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(CURRENT_DIR, 'db', 'nymdesign_home.db3') 

# Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

ADMINS = (('fname lname', 'email@email.com'),)

MEDIA_ROOT = os.path.join(CURRENT_DIR, 'static_media') 

MEDIA_URL = 'http://127.0.0.1:8000/media/'
#MEDIA_URL = 'http://10.0.1.194:8080/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = ''

ROOT_URLCONF = 'nymdesign.urls_test'

TEMPLATE_DIRS = (   os.path.join(CURRENT_DIR, 'nymdesign', 'templates'),
)
