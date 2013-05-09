pyagents
========

Installation
============
For the flu import to work:
    mkdir data
    wget http://54.235.153.252/data/admin0.json data/admin0.json
    wget http://54.235.153.252/data/admin1.json data/admin1.json

Usage
=====
Usage: python -m pyagents <agent> <action>

Testing
=====
We highly recommend nosetests for running the tests. i.e.

    $ cd /path/to/pyagents
    $ nosetests
