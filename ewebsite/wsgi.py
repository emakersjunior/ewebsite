"""
WSGI config for ewebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import time 
import traceback 
import signal 
import sys

from django.core.wsgi import get_wsgi_application

#sys.path.append('~/Projetos/ewebsite') 
# adjust the Python version in the line below as needed 
#sys.path.append('~/Projetos/.virtualenvs/ewebsite-env/lib/python3.5/site-packages') 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ewebsite.settings")

application = get_wsgi_application()
