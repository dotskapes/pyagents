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

import unittest
import os

from pyagents.adapters import PointOfNeedDiagnosticAdapter


class TestPointOfNeedDiagnosticAdaptor(unittest.TestCase):

    def setUp(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cur_path = os.path.join(cur_path, '..')
        self.data_path = os.path.join(cur_path, 'data')

    def test_benice(self):
        xml_name = os.path.join(self.data_path, 'benice.xml')
        json_name = os.path.join(self.data_path, 'benice.json')
        with open(xml_name, 'r') as cur_xml:
            contents = cur_xml.read()
            adapter = PointOfNeedDiagnosticAdapter()
            output = adapter.adapt(contents)
        with open(json_name, 'r') as cur_json:
            self.assertEqual(output, cur_json.read())

    def test_operator(self):
        xml_name = os.path.join(self.data_path, 'test_operator.xml')
        json_name = os.path.join(self.data_path, 'test_operator.json')
        with open(xml_name, 'r') as cur_xml:
            contents = cur_xml.read()
            adapter = PointOfNeedDiagnosticAdapter()
            output = adapter.adapt(contents)
        with open(json_name, 'r') as cur_json:
            self.assertEqual(output, cur_json.read())

if __name__ == '__main__':
    unittest.main()
