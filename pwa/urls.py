from django.urls import path

from .views import Manifest, ServiceWorker, OfflineView

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path('serviceworker.js', ServiceWorker.as_view(), name='serviceworker'),
    path('manifest.json', Manifest.as_view(), name='manifest'),
    path('offline', OfflineView.as_view(), name='offline')
]
