from http import HTTPStatus

from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed


def test_service_worker_get(client):
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


def test_offline_get(client):
    response = client.get(reverse("pwa:offline"), format="json")

    assert response.status_code == HTTPStatus.OK
