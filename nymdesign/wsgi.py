import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'nymdesign.settings_prod'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()