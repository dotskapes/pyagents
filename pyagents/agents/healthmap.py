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
import os
import ConfigParser

from pyagents.adapters import HealthmapAdapter
from base import BaseAgent


class HealthmapAgent(BaseAgent):
    """Agent for loading Healthmap Data from healthmap.org.
    """

    def __init__(self, settings):
        super(HealthmapAgent, self).__init__(settings)
        self.adapter = HealthmapAdapter()
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cur_path = os.path.join(cur_path, '..')
        self.config_path = os.path.join(cur_path, 'configs')

    def update(self):
        source_uri = self.settings['source_uri']
        if self.settings.get('mode') != 'testing':
            config = ConfigParser.ConfigParser()
            config.read(os.path.join(self.config_path, 'healthmap.local.ini'))
            source_uri += '?'
            test = config.items('production')
            for k, v in config.items('production'):
                if v != '':
                    source_uri += k + '=' + v +'&'
            source_uri = source_uri[:-1]
        server_output = urllib2.urlopen(source_uri)
        output = self.adapter.adapt(server_output.read())
        return output
