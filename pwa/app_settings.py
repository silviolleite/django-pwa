""" Settings required by django-progressive-web-app. """
from django.conf import settings
import os

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates', 'serviceworker.js'))

# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'MyApp')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'My Progressive Web App')
PWA_APP_ROOT_URL = getattr(settings, 'PWA_APP_ROOT_URL', '/')
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_START_URL = getattr(settings, 'PWA_APP_START_URL', '/')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    {
        'src': '/',
        'sizes': '160x160'
    }
])


