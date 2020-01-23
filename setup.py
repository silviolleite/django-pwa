import os
from setuptools import find_packages, setup

short_description = 'A Django app to include a manifest.json and Service Worker instance to enable progressive web ' \
                    'app behavior '

# noinspection PyBroadException
try:
    # noinspection PyPackageRequirements
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except ModuleNotFoundError:
    long_description = short_description

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requirements = [
    "django>=1.8",
]

setup(
    name='django-pwa',
    version='1.0.7',
    packages=find_packages(),
    install_requires=install_requirements,
    include_package_data=True,
    license='MIT License',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/silviolleite/django-pwa',
    author='Silvio Luis',
    author_email='silviolleite@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)