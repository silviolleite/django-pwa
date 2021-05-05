from django.utils import version

DJANGO_VERSION = version.get_version()

if (DJANGO_VERSION[0]) >= 2:
    from django.urls import re_path
else:
    from django.conf.urls import url as re_path

from .views import manifest, service_worker, offline

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    re_path(r"^serviceworker\.js$", service_worker, name="serviceworker"),
    re_path(r"^manifest\.json$", manifest, name="manifest"),
    re_path("^offline/$", offline, name="offline"),
]
