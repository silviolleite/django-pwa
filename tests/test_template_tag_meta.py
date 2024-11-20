import pytest
from django.template import Context, Template
from pytest_django.asserts import assertInHTML


@pytest.mark.parametrize(
    "tag",
    [
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-72x72.png" sizes="72x72">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-96x96.png" sizes="96x96">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-128x128.png" sizes="128x128">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-144x144.png" sizes="144x144">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-152x152.png" sizes="152x152">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-192x192.png" sizes="192x192">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-384x384.png" sizes="384x384">',
        '<link rel="apple-touch-icon" href="/static/images/icons/icon-512x512.png" sizes="512x512">',
        '<link rel="manifest" href="/manifest.json">',
        '<meta name="mobile-web-app-capable" content="yes">',
        '<meta name="theme-color" content="#000">',
        '<meta name="apple-mobile-web-app-capable" content="yes">',
        '<meta name="apple-mobile-web-app-title" content="MyApp">',
        '<meta name="application-name" content="MyApp">',
        '<meta name="apple-mobile-web-app-status-bar-style" content="default">',
        '<link rel="icon" sizes="512x512" href="/static/images/icons/icon-512x512.png">',
        '<link href="/static/images/icons/splash-640x1136.png" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-750x1334.png" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-1242x2208.png" media="(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-1125x2436.png" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-828x1792.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-1242x2688.png" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-1536x2048.png" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-1668x2224.png" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-1668x2388.png" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<link href="/static/images/icons/splash-2048x2732.png" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
        '<meta name="msapplication-TileColor" content="#fff">',
        '<meta name="msapplication-TileImage" content="/static/images/icons/icon-512x512.png">',
    ],
)
def test_has_tags(tag):
    context = Context({})
    template_to_render = Template("{% load pwa %}" "{% progressive_web_app_meta %}")
    rendered_template = template_to_render.render(context)

    assertInHTML(tag, rendered_template)


@pytest.mark.parametrize(
    "content",
    [
        '<script type="text/javascript">',
        "if ('serviceWorker' in navigator) {",
        "navigator.serviceWorker.register('/serviceworker.js', {",
        "scope: '/'",
        "}).then(function (registration) {",
        "console.log('django-pwa: ServiceWorker registration successful with scope: ', registration.scope);",
        "}, function (err) {",
        "console.log('django-pwa: ServiceWorker registration failed: ', err);",
        "});",
        "</script>",
    ],
)
def test_assert_has_serviceworker(content):
    context = Context({})
    template_to_render = Template("{% load pwa %}" "{% progressive_web_app_meta %}")
    rendered_template = template_to_render.render(context)

    assert content in rendered_template
