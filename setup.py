#!/usr/bin/env python3
NAME = "moke"
VERSION = "1.2.0"

from setuptools import setup

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License"
]

setup(
    name=NAME.lower(),
    version=VERSION,
    author="Marcin Cieslik",
    author_email="mcieslik@med.umich.edu",
    description="moke is not like make",
    keywords="make, ant, rake, paver, build, shell, argparse, bash",
    long_description=open('README.rst', 'r').read(),
    long_description_content_type="text/x-rst",
    url='http://mcieslik-mctp.github.io/moke',
    packages = ["moke"],
    package_dir = {"": "src"},
    package_data = {"moke": ["data/*"]},
    scripts = ["bin/moke"],
    include_package_data=True,
    zip_safe=False,
    license="BSD License",
    classifiers=CLASSIFIERS,
    python_requires='>=3.6',
)
