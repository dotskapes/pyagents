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
try:
    import json
except ImportError:
    import simplejson as json

from pyagents.adapters import HealthmapAdapter
from base import BaseAgent


class HealthmapAgent(BaseAgent):
    """Agent for loading Healthmap Data from healthmap.org.
    """

    def __init__(self, settings):
        super(HealthmapAgent, self).__init__(HealthmapAdapter, settings)
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cur_path = os.path.join(cur_path, '..')
        self.config_path = os.path.join(cur_path, 'configs')

    def getConfig(self):
        config = {}
        config_file = os.path.join(self.config_path, 'healthmap.json')
        with open(config_file, 'r') as cur_config:
            config = json.load(cur_config)
        local_config_file = os.path.join(self.config_path, 'healthmap.local.json')
        if os.path.isfile(local_config_file):
            with open(local_config_file, 'r') as cur_config:
                config.update(json.load(cur_config))
        else:
            print "Please create a healthmap.local.json and put the apikey there!"
        return config

    def update(self):
        source_uri = self.settings['base_uri']
        if self.settings.get('mode') != 'testing':
            local_config = self.getConfig()
            source_uri += '?'
            for k, v in local_config.items():
                if str(v) != '':
                    if isinstance(v, bool):
                        # Current Healthmap api only accepts lower case "false"
                        source_uri += k + '=' + str.lower(str(v)) + '&'
                    else:
                        source_uri += k + '=' + str(v) + '&'
            source_uri = source_uri[:-1]
        server_output = urllib2.urlopen(source_uri)
        output = self.adapter.adapt(server_output.read())
        name = 'healthmap'
        self.notifyListeners(name, output)
        return output
