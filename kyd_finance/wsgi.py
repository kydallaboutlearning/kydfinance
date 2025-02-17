import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Set the default settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kyd_finance.settings.prod')

# Get WSGI application
application = get_wsgi_application()

# Serve static files with Whitenoise
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), "staticfiles"))
