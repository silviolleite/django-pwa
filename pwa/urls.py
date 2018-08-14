from django.conf.urls import url
from .views import manifest, service_worker

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    url('^serviceworker.js$', service_worker),
    url('^manifest.json$', manifest)
]
