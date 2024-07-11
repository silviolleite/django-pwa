from django.http import HttpResponse
from django.shortcuts import render

from . import app_settings


def service_worker(request):  # noqa: ARG001
    with open(app_settings.PWA_SERVICE_WORKER_PATH) as serviceworker_file:
        return HttpResponse(
            serviceworker_file.read(),
            content_type="application/javascript",
        )


def manifest(request):
    return render(
        request,
        "manifest.json",
        {
            setting_name: getattr(app_settings, setting_name)
            for setting_name in dir(app_settings)
            if setting_name.startswith("PWA_")
        },
        content_type="application/json",
    )


def offline(request):
    return render(request, "offline.html")
