""" This module offers simple parsing of GTFS files """

from distutils.core import setup

setup(
    name='gtfs-parser',
    version='0.1',
    url='',
    license='MIT',
    author='emeric',
    author_email='emeric.vigier@gmail.com',
    description='Simple GTFS parser',
    install_requires=[
        'pandas',
    ],
)
