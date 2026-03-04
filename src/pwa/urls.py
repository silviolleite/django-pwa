from django.urls import path

from .views import manifest, offline, service_worker

app_name = "pwa"

urlpatterns = [
    path("serviceworker.js", service_worker, name="serviceworker"),
    path("manifest.json", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
]
