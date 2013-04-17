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

from pyagents.detectors import BaseDetector

class ThresholdDetector(BaseDetector):
    """ Check if data has reached a certain threshold """

    ONE = 1
    ALL = 2
    AVERAGE = 3

    def __init__(self):
        super(ThresholdDetector, self).__init__()

    def detect(self, data, threshold = 0, criteria = 1):
        """ Check for a threshold in a dataset

        :param data: An array of data points
        :param threshold: The minimum value that triggers a threshold
        :param criteria: The mode that determines how the threshold is calculated
        :returns: A boolean indicating if an alert should be triggered
        """
        if criteria == ThresholdDetector.ONE:
            for point in data:
                if point > threshold:
                    return True
            return False
        elif criteria == ThresholdDetector.ALL:
            for point in data:
                if point <= threshold:
                    return False
            return True
        elif criteria == ThresholdDetector.AVERAGE:
            mean = float(sum(data)) / float(len(data))
            return (mean > threshold)
