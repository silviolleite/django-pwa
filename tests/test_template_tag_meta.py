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
            '<link rel="apple-touch-icon" href="/" sizes="160x160">',
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
