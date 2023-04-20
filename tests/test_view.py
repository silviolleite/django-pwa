import sys
from contextlib import suppress
from importlib import import_module, reload
from django.test import TestCase, override_settings
from django.shortcuts import resolve_url as r


def helper__reload_module(m):
    with suppress(Exception):
        reload(sys.modules[m])
        import_module(m)


class ServiceWorkerTestCase(TestCase):
    def setUp(self):
        # reload app_settings with new settings
        helper__reload_module('pwa.app_settings')
        self.response = self.client.get(r('serviceworker'))
        self.content = self.response.content.decode()

    def test_url(self):
        """The serviceworker URL Should be /serviceworker.js"""
        self.assertEqual(r('serviceworker'), '/serviceworker.js')

    def test_get(self):
        """GET /serviceworker.js Should return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_content_type_js(self):
        """The content type Must be Javascript"""
        self.assertEqual(self.response['content-type'], 'application/javascript')


@override_settings(
    PWA_SERVICE_WORKER_MODE='path',
    PWA_SERVICE_WORKER_CACHE_KEY='test-pwa-',
    PWA_SERVICE_WORKER_EXTRA_FILES=['/my-custom-file.txt'],
    PWA_APP_ICONS=[],
)
class ServiceWorkerTest(ServiceWorkerTestCase):
    def test_content_offline_url(self):
        """GET /serviceworker.js Should contain the default offline url"""
        self.assertIn("var offlineUrl = '/offline/';", self.content)

    def test_content(self):
        """GET /serviceworker.js Should contain default values"""
        self.assertIn(
            "var staticCacheKey = 'django-pwa-';",
            self.content,
            msg='Fixed cache key')
        self.assertIn(
            "'/static/images/icons/icon-512x512.png',",
            self.content,
            msg='Default files')
        self.assertNotIn(
            "'/my-custom-file.txt'",
            self.content,
            msg='No extra files')


@override_settings(
    PWA_SERVICE_WORKER_MODE='template',
    PWA_SERVICE_WORKER_CACHE_KEY='test-pwa-',
    PWA_SERVICE_WORKER_EXTRA_FILES=['/my-custom-file.txt'],
    PWA_APP_ICONS=[],
)
class TemplatedServiceWorkerTest(ServiceWorkerTestCase):
    def test_content_offline_url(self):
        """GET /serviceworker.js Should contain the real offline url"""
        self.assertIn("var offlineUrl = '{}';".format(r('offline')), self.content)

    def test_content(self):
        """GET /serviceworker.js Should contain dynamic values"""
        self.assertIn(
            "var staticCacheKey = 'test-pwa-';",
            self.content,
            msg='Custom cache key')
        self.assertNotIn(
            "'/static/images/icons/icon-512x512.png',",
            self.content,
            msg='No default files')
        self.assertIn(
            "'/my-custom-file.txt'",
            self.content,
            msg='With extra files')


class ManifestTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('manifest'), format='json')

    def test_get(self):
        """GET /manifest.json Should return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_content_type_json(self):
        """The content type Must be JSON"""
        self.assertEqual(self.response['content-type'], 'application/json')

    def test_template(self):
        """Must have the template manifest.json"""
        self.assertTemplateUsed(self.response, 'manifest.json')

    def test_manifest_contains(self):
        """Must be the attributes to manifest.json"""
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
            '"status_bar":'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class OfflineTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('offline'))

    def test_get(self):
        """GET /offline Should return status code 200"""
        self.assertEqual(200, self.response.status_code)
