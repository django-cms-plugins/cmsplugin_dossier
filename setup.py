#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_dossier',
    version='0.0.1',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description = 'DjangoCMS dossier plugin - allows easy adding of personal data to the DjangoCMS',
    packages=find_packages(),
    provides=['cmsplugin_dossier',],
    include_package_data=True,
    install_requires = ['easy-thumbnails',]
)