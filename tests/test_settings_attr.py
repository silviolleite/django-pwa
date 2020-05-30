from django.test import TestCase
from pwa import app_settings


class AppSettingsTest(TestCase):
    def test_has_defined(self):
        """Must have the attributes defined in app_settings.py"""
        attributes = [
            'PWA_SERVICE_WORKER_PATH',
            'PWA_APP_NAME',
            'PWA_APP_DESCRIPTION',
            'PWA_APP_ROOT_URL',
            'PWA_APP_THEME_COLOR',
            'PWA_APP_BACKGROUND_COLOR',
            'PWA_APP_SCOPE',
            'PWA_APP_DISPLAY',
            'PWA_APP_ORIENTATION',
            'PWA_APP_START_URL',
            'PWA_APP_FETCH_URL',
            'PWA_APP_ICONS',
            'PWA_APP_DIR',
            'PWA_APP_LANG',
            'PWA_APP_STATUS_BAR_COLOR'
        ]
        for attr in attributes:
            with self.subTest():
                self.assertTrue(hasattr(app_settings, attr))
