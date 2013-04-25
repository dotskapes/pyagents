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


class BaseAgent(object):
    """Base class for agents. You only need an update and a constructor for
    this to work properly.
    """


    def __init__(self, Adapter=None, settings=None):
        """ Base constructor for all agents
        :param Adapter: The class of data adapter to use for this agent
        """
        super(BaseAgent, self).__init__()
        if Adapter:
            self.adapter = Adapter()
        if settings:
            self.settings = settings
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    def notifyListeners(self, name, output):
        """ notify listeners of output """
        for listener in self.listeners:
            listener(name, output)
