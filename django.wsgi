import os
import sys
sys.path.append('/var/www/html/rsyslogviewer')
os.environ['PYTHON_EGG_CACHE'] = '/var/www/html/rsyslogviewer/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
