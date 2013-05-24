pyagents
========

Installation
============
For the flu import to work:

    cd pyagents/pyagents

    wget http://54.235.153.252/data/admin0.json data/admin0.json
    
    wget http://54.235.153.252/data/admin1.json data/admin1.json

Usage
=====
Usage: 

    python -m pyagents <agent> <action>

where,
    action is "update"

    agent = "flu", "pon", "healthmap"


Testing (in beta)
=====
We highly recommend nosetests for running the tests. i.e.

    $ cd /path/to/pyagents
    $ nosetests
