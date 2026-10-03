import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "keyforge.settings")

from keyforge.wsgi import application

app = application
