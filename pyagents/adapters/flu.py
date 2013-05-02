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
import inspect

try:
    import json
except ImportError:
    import simplejson as json

import codecs

from base import BaseAdapter


class GoogleFluAdapter(BaseAdapter):
    def add_ref(self, path):
        referenceData = unicode(codecs.open(path,
                                encoding='latin-1',  mode='r').read())
        referenceGeom = json.loads(referenceData)
        for feature in referenceGeom['features']:
            name = feature['properties']['name']
            self.geomLookup[name] = feature['geometry']
            if feature['properties']['name_alt']:
                for alt in feature['properties']['name_alt'].split('|'):
                    if len(alt):
                        self.geomLookup[alt] = feature['geometry']
        
    def __init__(self):
        self.input = 'csv'
        self.output = 'json'

        self.geomLookup = {}

        base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        country_path = base_path +  '/../data/admin0.json'
        state_path = base_path +  '/../data/admin1.json'

        self.add_ref(country_path)
        self.add_ref(state_path)

    def adapt(self, data, country, disease):
        lines = data.split('\n')[11:]
        adminNames = lines[0].split(',')
        adminAttr = {}
        features = []

        countryAttr = {'state': None, 'country': country, 'disease': disease, 'admin': 0}
        for admin in adminNames[2:]:
            if admin in self.geomLookup:
                adminAttr[admin] = {'state': admin, 'country': country, 'disease': disease, 'admin': 1}
                print admin

        # Build the state level data
        for line in lines[1:]:
            if not len(line):
                continue
            line = line.split(',')
            timestep = line[0]
            if line[1]:
                countryAttr[timestep] = int(line[1])
            for admin, attr in zip(adminNames[2:], line[2:]):
                if admin in self.geomLookup:
                    if attr:
                        adminAttr[admin][timestep] = int(attr)

        for admin in adminAttr:
            feature = {
                'type': 'Feature',
                'properties': adminAttr[admin],
                'geometry': self.geomLookup[admin]}
            features.append(feature)

        features.append({
                'type': 'Feature',
                'properties': countryAttr,
                'geometry': self.geomLookup[country]
                })
        buffer = json.dumps({
            'type': 'FeatureCollection',
            'features': features})
        return buffer
