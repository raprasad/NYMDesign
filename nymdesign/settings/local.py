from __future__ import absolute_import
import json
import sys
from os import makedirs
from os.path import join, normpath, isdir, isfile
from .base import *

SECRET_KEY = "j#)2/N,So%0}W:fcrog%xAsVCb^BR,K<\g_e(@)VK9}h^`j,C}-xpbsZbX\^;m,"

LOCAL_SETUP_DIR = join(BASE_DIR, 'test_setup')
if not isdir(LOCAL_SETUP_DIR):
    makedirs(LOCAL_SETUP_DIR)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(LOCAL_SETUP_DIR, 'db2.sqlite3'),
    }
}

SESSION_COOKIE_NAME = 'nymdesign_local'

# where static files are collected
STATIC_ROOT = join(BASE_DIR, 'test_setup', 'assets')
if not isdir(STATIC_ROOT):
    makedirs(STATIC_ROOT)

MEDIA_ROOT = join(BASE_DIR, 'uploaded_media')
#MEDIA_ROOT = join(BASE_DIR, 'test_setup', 'media')
#if not isdir(MEDIA_ROOT):
#    makedirs(MEDIA_ROOT)

PAGE_CACHE_TIME = 0 # 0 for dev    //60 * 60 * 2 # 2 hours

ROOT_URLCONF = 'nymdesign.urls_test'


ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1']
