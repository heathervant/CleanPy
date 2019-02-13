#!/usr/bin/env python

from setuptools import setup

setup(
    name='CleanPy',
    url='https://github.com/UBC-MDS/CleanPy',
    author='Patrick Tung, Heather Van Tassel, Phuntsok Tseten',
    author_email='na',
    packages=['cleanpy'],
    install_requires=['numpy', 'pandas'],
    license='MIT',
    description='A package for cleaning messy data on Python'
)