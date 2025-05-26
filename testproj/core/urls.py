from django.urls import path

from .views import index

app_name = "testproj.core"

urlpatterns = [
    path("", index, name="index"),
]
