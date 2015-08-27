"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import  sys
import os

sys.path.append('/opt/blog')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
os.environ['PYTHON_EGG_CACHE'] ='/tmp'
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
