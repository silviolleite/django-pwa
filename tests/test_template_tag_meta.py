from django.test import TestCase
from django.template import Context, Template


class CreateMetaTemplateTagTest(TestCase):
    def setUp(self):
        context = Context({})
        template_to_render = Template(
            '{% load pwa %}'
            '{% progressive_web_app_meta %}'
        )
        self.rendered_template = template_to_render.render(context)

    def test_has_tags(self):
        """Must contains the tags in HTML"""
        tags = [
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-72x72.png" sizes="72x72">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-96x96.png" sizes="96x96">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-128x128.png" sizes="128x128">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-144x144.png" sizes="144x144">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-152x152.png" sizes="152x152">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-192x192.png" sizes="192x192">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-384x384.png" sizes="384x384">',
            '<link rel="apple-touch-icon" href="/static/images/icons/icon-512x512.png" sizes="512x512">',
            '<link rel="manifest" href="/manifest.json">',
            '<meta name="theme-color" content="#000">',
            '<meta name="apple-mobile-web-app-capable" content="yes">',
            '<meta name="apple-mobile-web-app-title" content="MyApp">',
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">'
        ]
        for text in tags:
            with self.subTest():
                self.assertInHTML(text, self.rendered_template)

    def test_has_serviceworker(self):
        """Must have the script tag with serviceworker registration"""
        contents = [
            '<script type="text/javascript">',
            "if ('serviceWorker' in navigator) {",
            "navigator.serviceWorker.register('/serviceworker.js', {",
            "scope: '.'",
            "}).then(function (registration) {",
            "console.log('django-progressive-web-app: ServiceWorker registration successful with scope: ', registration.scope);",
            "}, function (err) {",
            "console.log('django-progressive-web-app: ServiceWorker registration failed: ', err);",
            "});",
            "</script>"
        ]

        for expected in contents:
            with self.subTest():
                self.assertIn(expected, self.rendered_template)
