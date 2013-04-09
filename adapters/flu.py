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

from pyagents.base import BaseAdapter


class GoogleFluAdapter(BaseAdapter):
    def __init__(self):
        self.input = 'csv'
        self.output = 'json'

        self.geomLookup = {}

        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        referenceData = unicode(codecs.open(path + '/../data/admin1.json',
                                encoding='latin-1',  mode='r').read())
        referenceGeom = json.loads(referenceData)
        for feature in referenceGeom['features']:
            name = feature['properties']['name']
            self.geomLookup[name] = feature['geometry']
            for alt in feature['properties']['name_alt'].split('|'):
                if len(alt):
                    self.geomLookup[alt] = feature['geometry']

    def adapt(self, data):
        lines = data.split('\n')[11:]
        adminNames = lines[0].split(',')
        adminAttr = {}
        features = []

        for admin in adminNames:
            if admin in self.geomLookup:
                adminAttr[admin] = {'name': admin}
                print admin

        for line in lines[1:]:
            line = line.split(',')
            timestep = line[0]
            for admin, attr in zip(adminNames, line[1:]):
                if admin in self.geomLookup:
                    adminAttr[admin][timestep] = attr

        for admin in adminAttr:
            feature = {
                'type': 'Feature',
                'properties': adminAttr[admin],
                'geometry': self.geomLookup[admin]}
            features.append(feature)
        buffer = json.dumps({
            'type': 'FeatureCollection',
            'features': features})
        return buffer
