#!/usr/bin/env python

try:
    from setuptools import setup
    setuptools_available = True
except ImportError:
    from distutils.core import setup
    setuptools_available = False


params = {}


setup(
    name='cl_notify',
    version='0.0.1',
    packages=['cl_notify'],
    author='Brandon DeRosier',
    author_email='x@bdero.me',
    description='A desktop notification tool for craigslist searches.',
    url='https://github.com/bdero/cl-notify',
    install_requires=[
        "python-craigslist",
    ],

    **params
)
