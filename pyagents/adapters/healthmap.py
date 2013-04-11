
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

try:
    import json
except ImportError:
    import simplejson as json

from pyagents.adapters import BaseAdapter


class HealthmapAdapter(BaseAdapter):
    """Data adapter for handling the Healthmap data"""

    def __init__(self):
        super(HealthmapAdapter, self).__init__()

    def adapt(self, data):
        feature_collection = []
        healthmap_records = json.loads(data)

        for record in healthmap_records:
            loc = [float(record['lat']), float(record['lng'])]
            properties = {}
            properties['country'] = record['country']
            properties['place_name'] = record['place_name']
            for alert in record['alerts']:
                properties.update(alert)
                # change data into geojson format
                geometry = {'type': 'Point',
                            'coordinates': loc}
                feature = {'type': 'Feature',
                           'geometry': geometry,
                           'properties': properties}
                feature_collection.append(feature)
        return json.dumps({'type': 'FeatureCollection',
                           'features': [feature_collection]})
