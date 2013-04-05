import os
import inspect

import urllib2
from adapters import GoogleFluAdapter

countries = [
    'ar',
    'au',
    'at',
    'be',
    'bo',
    'br',
    'bg',
    'ca',
    'cl',
    'fr',
    'de',
    'hu',
    'jp',
    'mx',
    'nl',
    'nz',
    'no',
    'py',
    'pe',
    'pl',
    'ro',
    'ru',
    'za',
    'es',
    'se',
    'ch',
    'ua',
    'us',
    'uy'
    ]

class GoogleFluAgent:
    def __init__(self, settings):
        self.adapter = GoogleFluAdapter()
        self.settings = settings

    def update(self):
        for country in countries:
            input = urllib2.urlopen('http://www.google.org/flutrends/%s/data.txt' % (country,)).read()
            output = self.adapter.adapt(input)
            urllib2.urlopen('http://' + self.settings['host'] + ':' + str(self.settings['port']) + self.settings['path'] + '/data/write/flu/%s.json' % (country,), output)
