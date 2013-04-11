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

from base import BaseAgent
from pyagents.adapters import PointOfNeedDiagnosticAdapter


class PointOfNeedDiagnosticAgent(BaseAgent):
    """Data adapter for handling the HL7-ish DoD Point-of-Need Diagnostic
    Data. This will be consumed in consecutive XML packages from an endpoint
    hosted by MIT-LL."""

    def __init__(self, settings):
        super(PointOfNeedDiagnosticAgent, self).__init__(settings)
        self.adapter = PointOfNeedDiagnosticAdapter()

    def update(self):
        input_data = urllib2.urlopen(self.settings['source_uri']).read()
        output = self.adapter.adapt(input_data)
        return output
