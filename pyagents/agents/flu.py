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
import simplejson as json

from pyagents.agents import BaseAgent
from pyagents.adapters import GoogleFluAdapter
from pyagents.detectors import ThresholdDetector

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


def parse_iso_date(candidate):
    m = re.match('^(\d\d\d\d)-(\d\d)-(\d\d)$', candidate)
    if not m:
        return None
    date = datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return int(time.mktime(date.timetuple()))


class GoogleFluAgent(BaseAgent):
    def __init__(self, settings):
        super(GoogleFluAgent, self).__init__(GoogleFluAdapter, settings)
        self.base_url = 'http://www.google.org/flutrends'

    def update(self):
        ''' Update Google Flu Trends data. '''
        for country in countries:
            input = urllib2.urlopen(self.base_url + '/%s/data.txt' % (country,)).read()
            output = self.adapter.adapt(input)
            return super(GoogleFluAgent, self).update('flu/' + country + '.json', output)

    def detect(self):
        ''' Pull down a copy of all Google Flu data from the server
            Inspect the most current value for a threshold
        '''
        for country in countries:
            raw_data = urllib2.urlopen(self.datapath() + '/load/flu/%s.json' % (country,)).read()
            geodata = json.loads(raw_data)
            points = []
            detector = ThresholdDetector()
            for feature in geodata['features']:
                dates = []
                for key in feature['properties']:
                    timestamp = parse_iso_date(key)
                    if timestamp:
                        dates.append({
                                'key': key,
                                'timestamp': timestamp
                                })
                dates.sort(key = lambda x: x['timestamp'])
                if len(dates):
                    current_date = dates[-1]
                    points.append(int(feature['properties'][current_date['key']]))
            result = detector.detect(points, threshold = 1500)
            if result:
                print country
