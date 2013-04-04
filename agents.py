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
    def __init__(self):
        self.adapter = GoogleFluAdapter()

    def update(self):
        for country in countries:
            input = urllib2.urlopen('http://www.google.org/flutrends/%s/data.txt' % (country,)).read()
            output = self.adapter.adapt(input)

            # Write to scratch for now
            path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            stream = open(path + '/.scratch/%s.json' % (country,), 'w')
            stream.write(output)
            stream.close()
            
