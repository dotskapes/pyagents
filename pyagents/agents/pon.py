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

import requests

try:
    import json
except ImportError:
    import simplejson as json

from base import BaseAgent
from pyagents.adapters import PointOfNeedDiagnosticAdapter

from lxml.etree import XMLSyntaxError


class PointOfNeedDiagnosticAgent(BaseAgent):
    """Data adapter for handling the HL7-ish DoD Point-of-Need Diagnostic
    Data. This will be consumed in consecutive XML packages from an endpoint
    hosted by MIT-LL."""

    def __init__(self, settings):
        super(PointOfNeedDiagnosticAgent, self).__init__(PointOfNeedDiagnosticAdapter, settings)

    def update(self):
        query_url = '%s://%s:%d/%s/eds/query/%s/%s' % (self.settings['source_protocol'],
                                                       self.settings['source_host'],
                                                       self.settings['source_port'],
                                                       self.settings['source_path'],
                                                       self.settings['current_index'],
                                                       '9999999999')
        print query_url
        out = requests.get(query_url, auth=(self.settings['source_username'],
                                            self.settings['source_password']))

        features = []
        for text_id in out.text.split(','):
            get_url = '%s://%s:%d/%s/eds/%s' % (self.settings['source_protocol'],
                                                self.settings['source_host'],
                                                self.settings['source_port'],
                                                self.settings['source_path'],
                                                text_id)
            pon_obj = requests.get(get_url, auth=(self.settings['source_username'],
                                                  self.settings['source_password']))

            try:
                print 'Parsing PoN: %s' % text_id
                output = self.adapter.adapt(pon_obj.text)
                features.append(output)
            except XMLSyntaxError:
                print 'Parsing of PoN document %s Failed' % text_id
        return json.dumps({'type': 'FeatureCollection',
                           'features': features})
