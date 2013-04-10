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

import urllib2
from pyagents.adapters import GoogleFluAdapter

countries = [
    'ar',
    'au',
    'at',
    'be',
    'bo',
    'br',
    'bg',
    'ca',
    'cl',
    'fr',
    'de',
    'hu',
    'jp',
    'mx',
    'nl',
    'nz',
    'no',
    'py',
    'pe',
    'pl',
    'ro',
    'ru',
    'za',
    'es',
    'se',
    'ch',
    'ua',
    'us',
    'uy']


class GoogleFluAgent:
    def __init__(self, settings):
        self.adapter = GoogleFluAdapter()
        self.settings = settings

    def update(self):
        for country in countries:
            input = urllib2.urlopen('http://www.google.org/flutrends/%s/data.txt' % (country,)).read()
            output = self.adapter.adapt(input)
            urllib2.urlopen('http://' + self.settings['host'] + ':' + str(self.settings['port']) + self.settings['path'] + '/data/write/flu/%s.json' % (country,), output)
