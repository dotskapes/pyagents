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
import datetime

from pyagents.adapters import HealthmapAdapter
from base import BaseAgent


class HealthmapAgent(BaseAgent):
    """Agent for loading Healthmap Data from healthmap.org.
    """

    def __init__(self, settings):
        super(HealthmapAgent, self).__init__(HealthmapAdapter, settings,
                                             'healthmap')

    def update(self):
        base_uri = self.settings['base_uri']
        print(self.settings)
        if self.settings.get('mode') != 'testing':
            date_comps = self.settings['sdate'].split('-')
            date_comps = [int(comp) for comp in date_comps]
            sdate = datetime.date(date_comps[0], date_comps[1], date_comps[2])
            today = datetime.date.today()
            day = datetime.timedelta(days=1)
            while sdate < today:
                sdatestr = sdate.isoformat()
                self.settings['sdate'] = sdatestr
                self.settings['edate'] = (sdate + day).isoformat()
                source_uri = base_uri + '?'
                for k, v in self.settings.items():
                    if str(v) != '':
                        if isinstance(v, bool):
                            # Current Healthmap api only accepts lower case "false"
                            source_uri += k + '=' + str.lower(str(v)) + '&'
                        else:
                            source_uri += k + '=' + str(v) + '&'
                source_uri = source_uri[:-1]
                server_output = urllib2.urlopen(source_uri)
                out_string = server_output.read()
                try:
                    output = self.adapter.adapt(out_string)
                    self.notifyListeners(self.name, output)
                except ValueError:
                    print("No Data for %s" % sdatestr)
                sdate = sdate + day
        return output
