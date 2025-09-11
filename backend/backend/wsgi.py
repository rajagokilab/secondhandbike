import os
from django.core.wsgi import get_wsgi_application

# Adjust this path!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
