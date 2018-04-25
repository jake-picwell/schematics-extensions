#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'schematics==2.0.1',
]

setup(
    name='schematics-extensions',
    version='0.1.0',
    description='Extensions for the Schematics library',
    author='Picwell',
    author_email='dev@picwell.com',
    url='http://github.com/picwell/schematics-extensions',
    packages=find_packages(exclude=['*.test']),
    install_requires=requirements,
    include_package_data=True
)
