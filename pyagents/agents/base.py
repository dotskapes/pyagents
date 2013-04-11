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

    def __init__(self, settings):
        """Constructor. Be sure to setup the adapter in your implementation.
        """
        super(BaseAgent, self).__init__()
        self.adapter = None
        self.settings = settings

    def update(self):
        return NotImplemented