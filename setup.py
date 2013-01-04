#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.0.2'

setup(
    name='pycnb',
    version=__version__,
    description='pycnb',
    author='Jan Matejka',
    author_email='yac@blesmrt.net',
    url='https://github.com/yaccz/pycnb',

    packages = find_packages(
        where = '.'
    ),

    install_requires = [
        "cement",
        "twisted",
        "setuptools",
    ],

    entry_points = {
        'console_scripts': ['pycnb = pycnb.core:main']},
)
