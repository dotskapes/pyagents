import urllib2
import simplejson as json

from pyagents.agents.flu import countries, parse_iso_date
from pyagents.detectors import ThresholdDetector

class GoogleSignalAgent(object):
    """Takes geojson input and looks for a peak in the data. if peak
    found then sends out output"""

    def __init__(self, settings):
        self.settings = settings

    def datapath(self):
        """ Get the base path to the Canepi data api from the settings 
        should this be some sorta util fn? """
        return 'http://' + self.settings['host'] + ':' + str(self.settings['port']) + self.settings['path'] + '/data'


    def new_data(self,dummy1,dummy2):
        """notification that new data has come into the system
        grab new data and look for a peak"""
        
        for country in countries.keys():
            qtCountry = urllib2.quote(country)
            path = self.datapath() + '/load/goog?query=%s' % (qtCountry,)
            raw_data = urllib2.urlopen(path).read()
            geodata = json.loads(raw_data)
            points = []
            # todo: make detector configurable, threshold or peak
            detector = ThresholdDetector()
            for feature in geodata['features']:
                dates = []
                for key in feature['properties']:
                    timestamp = parse_iso_date(key)
                    if timestamp:
                        dates.append({
                                'key': key,
                                'timestamp': timestamp
                                })
                dates.sort(key = lambda x: x['timestamp'])
                if len(dates):
                    current_date = dates[-1]
                    points.append(int(feature['properties'][current_date['key']]))
            result = detector.detect(points, threshold = 1500)
            if result:
                print country
        
