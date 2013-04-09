#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#
# Library:   pyagents
#
# Copyright 2013 Canepi Team
#
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 ( the "License" );
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################

import os
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
    print("Don't do this")
    #os.system('python setup.py sdist upload')
    sys.exit()

packages = ['pyagents']

version = '0.0.1'

requires = ['lxml']

setup(name='pyagents',
    version=version,
    description='A framework for data access and monitoring agents.',
    long_description=open('README.md').read(),
    author='Canepi Team',
    author_email='team@canepi.org',
    url='http://github.com/dotskapes/pyagents',
    packages=packages,
    install_requires=requires,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ),
    )
