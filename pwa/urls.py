from django.urls import path, re_path

from .views import manifest, offline, service_worker

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    re_path(r"^serviceworker\.js$", service_worker, name="serviceworker"),
    re_path(r"^manifest\.json$", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
]
