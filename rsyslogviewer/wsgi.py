import os

os.environ["DJANGO_SETTINGS_MODULE"] = "rsyslogviewer.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
