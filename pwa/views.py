from django.http import HttpResponse
from django.shortcuts import render, resolve_url

from . import app_settings


def service_worker(request):
    try:
        if app_settings.PWA_SERVICE_WORKER_MODE == 'template':
            # get the list of "cached" entries
            _files = [
                # the icons
                *[icon['src'] for icon in app_settings.PWA_APP_ICONS],
                # the splash screens
                *[screen['src'] for screen in app_settings.PWA_APP_SPLASH_SCREEN],
                # other files
                *app_settings.PWA_SERVICE_WORKER_EXTRA_FILES,
            ]

            return render(
                request,
                app_settings.PWA_SERVICE_WORKER_TEMPLATE,
                {
                    'pwa_offline_url': resolve_url('offline'),
                    'pwa_cache_key': app_settings.PWA_SERVICE_WORKER_CACHE_KEY,
                    'pwa_cached_files': _files,
                },
                content_type='application/javascript',
            )

        return HttpResponse(
            open(app_settings.PWA_SERVICE_WORKER_PATH).read(),
            content_type='application/javascript'
        )

    except Exception:
        # return an empty js file with any error
        return HttpResponse('', content_type='application/javascript')


def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    }, content_type='application/json')


def offline(request):
    return render(request, "offline.html")
