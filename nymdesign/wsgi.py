import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'nymdesign.settings.webfaction'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
