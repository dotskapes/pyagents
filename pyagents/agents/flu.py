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

import re
import datetime
import time
import urllib2

try:
    import json
except ImportError:
    import simplejson as json

from pyagents.agents import BaseAgent
from pyagents.adapters import GoogleFluAdapter
from pyagents.detectors import ThresholdDetector

countries = {
    'Argentina': 'ar',
    'Australia': 'au',
    'Austria': 'at',
    'Belgium': 'be',
    'Bolivia': 'bo',
    'Brazil': 'br',
    'Bulgaria': 'bg',
    'Canada': 'ca',
    'Chile': 'cl',
    'France': 'fr',
    'Germany': 'de',
    'Hungary': 'hu',
    'Japan': 'jp',
    'Mexico': 'mx',
    'Netherlands': 'nl',
    'New Zealand': 'nz',
    'Norway': 'no',
    'Paraguay': 'py',
    'Peru': 'pe',
    'Poland': 'pl',
    'Romania': 'ro',
    'Russia': 'ru',
    'South Africa': 'za',
    'Spain': 'es',
    'Sweden': 'se',
    'Switzerland': 'ch',
    'Ukraine': 'ua',
    'United States': 'us',
    'Uruguay': 'uy',
    }

def parse_iso_date(candidate):
    m = re.match('^(\d\d\d\d)-(\d\d)-(\d\d)$', candidate)
    if not m:
        return None
    date = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return int(time.mktime(date.timetuple()))


class GoogleFluAgent(BaseAgent):
    interval = 10000
    def __init__(self, settings):
        super(GoogleFluAgent, self).__init__(GoogleFluAdapter, settings)
        self.base_url = 'http://www.google.org/flutrends'
        self.disease = 'Flu'

    def update(self):
        """ Update Google Flu Trends data. """
        for country in countries:
            code = countries[country]
            input = urllib2.urlopen(self.base_url + '/%s/data.txt' % (code,)).read()
            output = self.adapter.adapt(input, country, self.disease)
            name = 'goog'
            super(GoogleFluAgent, self).notifyListeners(name, output)
