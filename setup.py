#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'schematics==1.1.1',
]

setup(name='schematics-extensions',
      version='0.0.5',
      description='Extensions for the Schematics library',
      author='Picwell',
      author_email='dev@picwell.com',
      url='http://github.com/picwell/schematics-extensions',
      packages=find_packages(),
      install_requires=requirements)
