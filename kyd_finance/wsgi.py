"""
WSGI config for kyd_finance project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kyd_finance.settings.prod')

application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application
from waitress import serve

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Get the WSGI application for your Django project
application = get_wsgi_application()

if __name__ == "__main__":
    # Use Waitress to serve the application
    serve(application, host='0.0.0.0', port=8000)
