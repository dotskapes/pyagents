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

class BaseDetector(object):
    ''' Base class for all detector. Abstractly, a detector takes data and determines if
        certain criteria have been met to determine if an agent should trigger an alert
    '''

    def __init__(self):
        super(BaseDetector, self).__init__()
        
    def detect(self, data, **kwargs):
        ''' Check if input data some property 

        :param data: A (detector specific) set of data to check
        :param kwargs: Detector specific arguments to invoke the watcher
        :returns: A boolean indicating if an alert should be triggered
        '''
        raise NotImplementedError()
