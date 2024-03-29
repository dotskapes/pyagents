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

from sys import argv

from agents import *
from manager import AgentManager

settings = {
    'host': '127.0.0.1',
    'port': 8080,
    'path': '/canepi',
    'base_uri': 'http://healthmap.org/HMapi.php',
}

config = {
    'agent': {
        'name': 'flu',
        'level': 1,
        'feature': 'Indiana'
        },
    'detector': {
        'name': 'threshold',
        'threshold': 1500
        }
    }

if __name__ == '__main__':
    if len(argv) == 1:
        manager = AgentManager(settings)
        manager.run()
    else:
        canepi = CanepiAgent(settings)
        if argv[1] == 'healthmap':
            agent = HealthmapAgent(settings)
        elif argv[1] == 'flu':
            agent = GoogleFluAgent(settings)
        elif argv[1] == 'pon':
            agent = PointOfNeedDiagnosticAgent(settings)

        if argv[2] == 'update':
            agent.addListener(canepi.update)
            agent.update()
