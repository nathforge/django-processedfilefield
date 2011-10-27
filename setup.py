#!/usr/bin/env python

from setuptools import setup
import os
import sys

PACKAGE_PATH = 'src'

sys.path.insert(0, PACKAGE_PATH)
import processedfilefield

setup(
    name='django-processedfilefield',
    url='https://github.com/nathforge/django-processedfilefield',
    version=processedfilefield.version_string(),
    description='Post-processing for Django FileFields.',
    long_description=open('README.txt').read(),
    
    author='Nathan Reynolds',
    author_email='email@nreynolds.co.uk',
    
    packages=['processedfilefield'],
    package_dir={'': PACKAGE_PATH},
)
