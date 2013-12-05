#!/usr/bin/env python2
# -*- coding: utf-8 -*-
NAME = "moke"
VERSION = "1.1.6"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 2.7",
    "License :: OSI Approved :: BSD License"
    ]

setup(
    name=NAME.lower(),
    version=VERSION,
    description="moke is not like make",
    keywords="make, ant, rake, paver, build, shell, argparse, bash",
    author="Marcin Cieslik",
    author_email="mcieslik-mctp@med.umich.edu",
    license="BSD License",
    long_description=open('README.rst', 'r').read(),
    classifiers=CLASSIFIERS,
    packages = ["moke"],
    package_dir = {"": "src"},
    package_data = {"moke": ["data/*"]},
    scripts = ["bin/moke"],
    # Options
    include_package_data=True,
    zip_safe=False,
    )
