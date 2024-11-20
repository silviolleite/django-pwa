import pytest

from pwa import app_settings


@pytest.mark.parametrize(
    "attribute",
    [
        "PWA_SERVICE_WORKER_PATH",
        "PWA_APP_NAME",
        "PWA_APP_DESCRIPTION",
        "PWA_APP_ROOT_URL",
        "PWA_APP_THEME_COLOR",
        "PWA_APP_BACKGROUND_COLOR",
        "PWA_APP_SCOPE",
        "PWA_APP_DISPLAY",
        "PWA_APP_ORIENTATION",
        "PWA_APP_START_URL",
        "PWA_APP_FETCH_URL",
        "PWA_APP_ICONS",
        "PWA_APP_DIR",
        "PWA_APP_LANG",
        "PWA_APP_STATUS_BAR_COLOR",
        "PWA_APP_SCREENSHOTS",
        "PWA_APP_SHORTCUTS",
    ],
)
def test_has_defined(attribute):
    """Must have the attributes defined in app_settings.py"""
    assert hasattr(app_settings, attribute)
