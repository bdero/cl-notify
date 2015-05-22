#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    setuptools_available = True
except ImportError:
    from distutils.core import setup, find_packages
    setuptools_available = False


params = {}

with open('README.md') as readme:
    params.update({'long_description': readme.read()})

with open('test_requirements.txt') as test_requirements:
    params.update({'tests_require': test_requirements.read_lines()})


setup(
    name='cl_notify',
    version='0.0.1',
    packages=['cl_notify'],
    author='Brandon DeRosier',
    author_email='x@bdero.me',
    description='A desktop notification tool for craigslist searches.',
    url='https://github.com/bdero/cl-notify',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        "python-craigslist",
    ],

    **params
)
