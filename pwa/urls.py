from django import VERSION


from .views import manifest, service_worker, offline

if VERSION >= (4, 0):
    from django.urls import path

    urlpatterns = [
        path('serviceworker.js', service_worker, name='serviceworker'),
        path('manifest.json', manifest, name='manifest'),
        path('offline/', offline, name='offline')
    ]

else:
    from django.urls import re_path

    # Serve up serviceworker.js and manifest.json at the root
    urlpatterns = [
        re_path(r'^serviceworker\.js$', service_worker, name='serviceworker'),
        re_path(r'^manifest\.json$', manifest, name='manifest'),
        re_path('^offline/$', offline, name='offline')
    ]
