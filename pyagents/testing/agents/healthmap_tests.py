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

from pyagents.agents import HealthmapAgent


class TestHealthmapAgent(unittest.TestCase):

    def test_seven_days(self):
        settings = {'host': '127.0.0.1',
                    'port': 8888,
                    'path': '/fudd',
                    'source_uri': 'http://healthmap.org/HMapi.php',
                    'auth_token': ''}
        agent = HealthmapAgent(settings)
        output = agent.update()
        print output
