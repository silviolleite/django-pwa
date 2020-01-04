django-pwa
=====
[![Build Status](https://travis-ci.org/silviolleite/django-pwa.svg)](https://travis-ci.org/silviolleite/django-pwa)
[![Maintainability](https://api.codeclimate.com/v1/badges/246542ea921058c4f76f/maintainability)](https://codeclimate.com/github/silviolleite/django-pwa/maintainability)
[![codecov](https://codecov.io/gh/silviolleite/django-pwa/branch/master/graph/badge.svg)](https://codecov.io/gh/silviolleite/django-pwa) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-pwa.svg)](https://pypi.org/project/django-pwa/)
[![PyPI - Downloads](https://img.shields.io/pypi/v/django-pwa.svg)](https://pypi.org/project/django-pwa)
[![PyPI - Downloads](https://img.shields.io/pypi/djversions/django-pwa.svg)](https://pypi.org/project/django-pwa)

This Django app turns your project into a [progressive web app](https://developers.google.com/web/progressive-web-apps/).  Navigating to your site on an Android phone will prompt you to add the app to your home screen.

![Prompt for install](https://github.com/silviolleite/django-pwa/raw/master/images/screenshot1.png)

Launching the app from your home screen will display your app [without browser chrome](https://github.com/silviolleite/django-pwa/raw/master/images/screenshot2.png).  As such, it's critical that your application provides all navigation within the HTML (no reliance on the browser back or forward button).

Requirements
=====
Progressive Web Apps require HTTPS unless being served from localhost.  If you're not already using HTTPS on your site, check out [Let's Encrypt](https://letsencrypt.org/) and [ZeroSSL](https://zerossl.com/).

Installation
=====
Install from PyPI:

```
pip install django-pwa
```

Configuration
=====
Add `pwa` to your list of `INSTALLED_APPS` in settings.py:

```python
INSTALLED_APPS = [
    ...
    'pwa',
    ...
]
```
Define STATICFILES_DIRS for your custom PWA_APP_ICONS
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

Configure your app name, description, icons and splash screen images in settings.py:
```python

PWA_APP_NAME = 'My App'
PWA_APP_DESCRIPTION = "My app description"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/images/my_app_icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/my_apple_icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

```
#### Show console.log
Set the `PWA_APP_DEBUG_MODE = False` to disable the the `console.log` on browser. 

All settings are optional, and the app will work fine with its internal defaults.  Highly recommend setting at least `PWA_APP_NAME`, `PWA_APP_DESCRIPTION`, `PWA_APP_ICONS` and `PWA_APP_SPLASH_SCREEN`.

Add the progressive web app URLs to urls.py:
```python
from django.urls import url, include

urlpatterns = [
    ...
    url('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    ...
]
```

Inject the required meta tags in your base.html (or wherever your HTML &lt;head&gt; is defined):
```html
{% load pwa %}

<head>
    ...
    {% progressive_web_app_meta %}
    ...
</head>
```

Troubleshooting
=====
While running the Django test server:

1. Verify that `/manifest.json` is being served
1. Verify that `/serviceworker.js` is being served
1. Verify that `/offline` is being served
1. Use the Application tab in the Chrome Developer Tools to verify the progressive web app is configured correctly.
1. Use the "Add to homescreen" link on the Application Tab to verify you can add the app successfully.


The Service Worker
=====
By default, the service worker implemented by this app is:
```js
// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline',
    '/css/django-pwa-app.css',
    '/images/icons/icon-72x72.png',
    '/images/icons/icon-96x96.png',
    '/images/icons/icon-128x128.png',
    '/images/icons/icon-144x144.png',
    '/images/icons/icon-152x152.png',
    '/images/icons/icon-192x192.png',
    '/images/icons/icon-384x384.png',
    '/images/icons/icon-512x512.png',
    '/static/images/icons/splash-640x1136.png',
    '/static/images/icons/splash-750x1334.png',
    '/static/images/icons/splash-1242x2208.png',
    '/static/images/icons/splash-1125x2436.png',
    '/static/images/icons/splash-828x1792.png',
    '/static/images/icons/splash-1242x2688.png',
    '/static/images/icons/splash-1536x2048.png',
    '/static/images/icons/splash-1668x2224.png',
    '/static/images/icons/splash-1668x2388.png',
    '/static/images/icons/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});
```

Adding Your Own Service Worker
=====
To add service worker functionality, you'll want to create a `serviceworker.js` or similarly named template in a template directory, and then point at it using the PWA_SERVICE_WORKER_PATH variable (PWA_APP_FETCH_URL is passed through).

```python
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'my_app', 'serviceworker.js')

```

The offline view
=====
By default, the offline view is implemented in `templates/offline.html`
You can overwrite it in a template directory if you continue using the default `serviceworker.js`.  


Feedback
=====
I welcome your feedback and pull requests.  Enjoy!

License
=====
All files in this repository are distributed under the MIT license.
