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

from pyagents.adapters import HealthmapAdapter
from base import BaseAgent


class HealthmapAgent(BaseAgent):
    """Agent for loading Healthmap Data from healthmap.org.
    """

    def __init__(self, settings):
        super(HealthmapAgent, self).__init__(settings)
        self.adapter = HealthmapAdapter()

    def update(self):
        server_output = urllib2.urlopen('%s?auth=%s&striphtml=1' % (
            self.settings['source_uri'], self.settings['auth_token']))
        output = self.adapter.adapt(server_output.read())
        return output
