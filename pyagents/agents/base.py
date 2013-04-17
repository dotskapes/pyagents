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

class BaseAgent(object):
    """Base class for agents. You only need an update and a constructor for
    this to work properly.
    """

    def __init__(self, Adapter, settings):
        """ Base constructor for all agents
        :param Adapter: The class of data adapter to use for this agent
        :param settings: Connection information for the Canepi api
        """
        super(BaseAgent, self).__init__()
        self.adapter = Adapter()
        self.settings = settings

    def datapath(self):
        """ Get the base path to the Canepi data api from the settings """
        return 'http://' + self.settings['host'] + ':' + str(self.settings['port']) + self.settings['path'] + '/data'

    def update(self, name, input_data):
        """ Push a write to the Canepi api through an HTTP request """
        path = self.datapath() + '/write/%s' % (name,)
        return urllib2.urlopen(path, input_data).read()

