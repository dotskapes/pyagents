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

import time

# For now, just import everything manually, later, do this smarter
from pyagents.agents import GoogleFluAgent, PointOfNeedDiagnosticAgent, CanepiAgent, GoogleSignalAgent
from pyagents.detectors import ThresholdDetector

def minIndex(array):
    min_value = float('inf')
    min_index = -1
    for i, item in enumerate(array):
        if item < min_value:
            min_value = item
            min_index = i
    return min_index

class AgentManager(object):
    """ Manages the set of alive agents"""

    def __init__(self, settings):
        # For now, just hard code the names
        self.__timer_agents = {
            'flu': GoogleFluAgent(),
            #'pon': PointOfNeedDiagnosticAgent()
            }
        self._detectors = {
            'threshold': ThresholdDetector()
            }
        self.wireUpAgents(settings)

    def wireUpAgents(self,settings):
        ''' hard wire up for now '''
        canepi = CanepiAgent(settings)
        # all src agents send data to canepi
        for src_agent in self.__timer_agents.values():
            src_agent.addListener(canepi.update)
        detector = GoogleSignalAgent(settings)
        canepi.addListener(detector.new_data)

    def agent(self, name):
        """ Retrieve an agent from the manager by name """
        return self.__timer_agents[name]

    def detector(self, name):
        """ Retrieve a detector from the manager by name """
        return self._detectors[name]

    def run(self):
        """ Start the main loop of the manager. Update agents at intervals. Never return """
        agent_list = self.__timer_agents.values()
        # Update every once initially: Next update 0 seconds from now
        next_updates = map(lambda x: 0, agent_list)
        while True:
            # Find the index of the agent (and time delta) closest to an update time
            update_index = minIndex(next_updates)
            delta = next_updates[update_index]
            # Wake up when the waiting time has passed
            time.sleep(delta)
            # Perform the actual update of the agent's data
            agent_list[update_index].update()
            # Reflect the amount of time waited in update times
            next_updates = map(lambda x: x - delta, next_updates)
            # Reset the waiting time on the agent we just updated
            next_updates[update_index] = agent_list[update_index].interval
