import os

# Pokud se settings nachází v /srv/app/shm,
# bude obsah pro DJANGO_SETTINGS_MODULE: shm.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shm.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
