from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pwa.urls", namespace="pwa")),
    path("", include("testproj.core.urls", namespace="core")),
]
