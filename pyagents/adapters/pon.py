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
from lxml import etree
import os


try:
    import json
except ImportError:
    import simplejson as json

from pyagents.adapters import BaseAdapter


class PointOfNeedDiagnosticAdapter(BaseAdapter):
    """Data adapter for handling the HL7-ish DoD Point-of-Need Diagnostic
    Data. This will be consumed in consecutive XML packages from an endpoint
    hosted by MIT-LL."""

    def __init__(self):
        super(PointOfNeedDiagnosticAdapter, self).__init__()

    def _get_parser_with_schema(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cur_path = os.path.join(cur_path, '..')
        cur_path = os.path.join(cur_path, 'resources')
        schema_path = os.path.join(cur_path, 'DiagDeviceRespiratoryPanel.xsd')
        with open(schema_path, 'r') as schema_contents:
            schema_xml = etree.XML(schema_contents.read())
            schema = etree.XMLSchema(schema_xml)
            parser = etree.XMLParser(schema=schema)
            return parser

    def adapt(self, data):

        # Parse XML and load properties.
        parser = self._get_parser_with_schema()
        root = etree.fromstring(data, parser)
        header_properties = dict()
        footer_properties = dict()
        diseases_by_name = dict()
        diseases_by_loinc = dict()
        loc = [0, 0]
        for node in root:
            if node.tag == 'Header':
                for child in node.getchildren():
                    if child.tag == 'Location':
                        lat = float(child.find('Latitude').text)
                        lon = float(child.find('Longitude').text)
                        loc = [lat, lon]
                    else:
                        header_properties[child.tag] = child.text
            elif node.tag == 'Footer':
                for child in node.getchildren():
                    footer_properties[child.tag] = child.text
            elif node.tag == 'LineDetail':
                test_name = node.find('Test').text
                loinc = node.find('LOINC').text
                result = node.find('Result').text
                diseases_by_name[test_name] = result
                if loinc != 'unknown':
                    diseases_by_loinc[loinc] = result  # Not using this yet

        # Push the data into geojson
        geometry = {'type': 'Point',
                    'coordinates': loc}
        feature = {'type': 'Feature',
                   'geometry': geometry,
                   'properties': dict(header_properties.items() +
                                      diseases_by_name.items() +
                                      footer_properties.items())}
        return json.dumps({'type': 'FeatureCollection',
                           'features': [feature]})
