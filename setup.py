import os
from setuptools import find_packages, setup

short_description = 'A Django app to include a manifest.json and Service Worker instance to enable progressive web ' \
                    'app behavior '

# noinspection PyBroadException
try:
    # noinspection PyPackageRequirements
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = short_description

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-progressive-web-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description=short_description,
    long_description=long_description,
    url='http://github.com/svvitale/django-progressive-web-app',
    author='Scott Vitale',
    author_email='svvitale@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)