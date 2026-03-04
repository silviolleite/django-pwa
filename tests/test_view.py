from http import HTTPStatus

import django
import pytest
from django.test import modify_settings
from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed


def test_service_worker_get(client):
    response = client.get(reverse("pwa:serviceworker"))

    assert response.status_code == HTTPStatus.OK


@pytest.mark.skipif(django.VERSION < (5, 1), reason="LoginRequiredMiddleware was introduced on Django 5.1")
def test_service_worker_get_unauthenticated(client):
    with modify_settings(
        MIDDLEWARE={
            "append": "django.contrib.auth.middleware.LoginRequiredMiddleware",
        }
    ):
        response = client.get(reverse("pwa:serviceworker"))

    assert response.status_code == HTTPStatus.OK


def test_manifest_get(client):
    response = client.get(reverse("pwa:manifest"), format="json")

    assert response.status_code == HTTPStatus.OK
    assert response["content-type"] == "application/json"
    assertTemplateUsed(response, "manifest.json")
    contents = [
        '"name":',
        '"short_name":',
        '"description":',
        '"start_url":',
        '"display":',
        '"scope":',
        '"background_color":',
        '"theme_color":',
        '"orientation":',
        '"icons":',
        '"dir":',
        '"lang":',
        '"status_bar":',
        '"screenshots" :',
        '"shortcuts" :',
    ]
    for expected in contents:
        assertContains(response, expected)


@pytest.mark.skipif(django.VERSION < (5, 1), reason="LoginRequiredMiddleware was introduced on Django 5.1")
def test_manifest_get_unauthenticated(client):
    response = client.get(reverse("pwa:manifest"), format="json")

    assert response.status_code == HTTPStatus.OK
    assert response["content-type"] == "application/json"


def test_offline_get(client):
    response = client.get(reverse("pwa:offline"), format="json")

    assert response.status_code == HTTPStatus.OK


@pytest.mark.skipif(django.VERSION < (5, 1), reason="LoginRequiredMiddleware was introduced on Django 5.1")
def test_offline_get_unauthenticated(client):
    with modify_settings(
        MIDDLEWARE={
            "append": "django.contrib.auth.middleware.LoginRequiredMiddleware",
        }
    ):
        response = client.get(reverse("pwa:offline"), format="json")

    assert response.status_code == HTTPStatus.OK
