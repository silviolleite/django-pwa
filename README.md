django-progressive-web-app
=====
This Django app turns your project into a [progressive web app](https://developers.google.com/web/progressive-web-apps/).  Navigating to your site on an Android phone will prompt you to add the app to your home screen.

![Prompt for install](https://github.com/svvitale/django-progressive-web-app/raw/master/images/screenshot1.png)

Launching the app from your home screen will display your app [without browser chrome](https://github.com/svvitale/django-progressive-web-app/raw/master/images/screenshot2.png).  As such, it's critical that your application provides all navigation within the HTML (no reliance on the browser back or forward button).

Requirements
=====
Progressive Web Apps require HTTPS unless being served from localhost.  If you're not already using HTTPS on your site, check out [Let's Encrypt](https://letsencrypt.org/) and [ZeroSSL](https://zerossl.com/).

Installation
=====
Install from PyPI:

```
pip install django-progressive-web-app
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

Configure your app name, description, and icons in settings.py:
```python
PWA_APP_NAME = 'My Kickass App'
PWA_APP_DESCRIPTION = "Do kickass things all day long without that pesky browser chrome"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/images/my_app_icon.png',
        'sizes': '160x160'
    }
]
```

All settings are optional, and the app will work fine with its internal defaults.  Highly recommend setting at least `PWA_APP_NAME` and `PWA_APP_DESCRIPTION`.

Add the progressive web app URLs to urls.py:
```python
from django.conf.urls import url, include

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
1. Use the Application tab in the Chrome Developer Tools to verify the progressive web app is configured correctly.
1. Use the "Add to homescreen" link on the Application Tab to verify you can add the app successfully.

Adding Your Own Service Worker
=====
By default, the service worker implemented by this app is empty.  To add service worker functionality, you'll want to create a `serviceworker.js` or similarly named file, and then point at it using the PWA_SERVICE_WORKER_PATH variable.

```python
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'my_app', 'serviceworker.js')

```

Feedback
=====
I welcome your feedback and pull requests.  Enjoy!

License
=====
All files in this repository are distributed under the MIT license.
