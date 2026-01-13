"""
WSGI config for visualizador_alumed project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visualizador_alumed.settings')

application = get_wsgi_application()
