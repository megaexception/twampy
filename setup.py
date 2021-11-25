#!/usr/bin/env python

from distutils.core import setup

setup(
    name='twampy',
    version='1.0',
    description='Python implementation of the Two-Way Active Measurement Protocol',
    author='Sven Wisotzky',
    author_email='sven.wisotzky(at)nokia.com',
    url='https://git.is.local/skhalavchuk/twampy.git',
    packages=['twampy'],
    entry_points={
        'console_scripts': [
            'twampy=twampy.twampy:main',
        ],
    },
    include_package_data=True,
)
