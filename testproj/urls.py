from django.urls import include, path

urlpatterns = [
    path("", include("pwa.urls", namespace="pwa")),
]
