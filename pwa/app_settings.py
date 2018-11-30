""" Settings required by django-app. """
from django.conf import settings
import os

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH', 'serviceworker.js')

# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'MyApp')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'My Progressive Web App')
PWA_APP_ROOT_URL = getattr(settings, 'PWA_APP_ROOT_URL', '/')
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_BACKGROUND_COLOR = getattr(settings, 'PWA_APP_BACKGROUND_COLOR', '#fff')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_ORIENTATION = getattr(settings, 'PWA_APP_ORIENTATION', 'any')
PWA_APP_START_URL = getattr(settings, 'PWA_APP_START_URL', '/')
PWA_APP_FETCH_URL = getattr(settings, 'PWA_APP_FETCH_URL', '/')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    {
        'src': '/static/images/icons/icon-72x72.png',
        'sizes': '72x72'
    },
    {
        'src': '/static/images/icons/icon-96x96.png',
        'sizes': '96x96'
    },
    {
        'src': '/static/images/icons/icon-128x128.png',
        'sizes': '128x128'
    },
    {
        'src': '/static/images/icons/icon-144x144.png',
        'sizes': '144x144'
    },
    {
        'src': '/static/images/icons/icon-152x152.png',
        'sizes': '152x152'
    },
    {
        'src': '/static/images/icons/icon-192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/icons/icon-384x384.png',
        'sizes': '384x384'
    },
    {
        'src': '/static/images/icons/icon-512x512.png',
        'sizes': '512x512'
    }
])
PWA_APP_DIR = getattr(settings, 'PWA_APP_DIR', 'auto')
PWA_APP_LANG = getattr(settings, 'PWA_APP_LANG', 'en-US')


