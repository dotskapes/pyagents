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

class CanepiAgent(object):
    """Agent that takes input and writes it to canepi"""

    def __init__(self, settings):
        self.settings = settings

    def datapath(self):
        """ Get the base path to the Canepi data api from the settings """
        return 'http://' + self.settings['host'] + ':' + str(self.settings['port']) + self.settings['path'] + '/data'


    def update(self, name, input_data):
        """ Push a write to the Canepi api through an HTTP request, returns status """
        path = self.datapath() + '/write/%s' % (name,)
        return urllib2.urlopen(path, input_data).read()
