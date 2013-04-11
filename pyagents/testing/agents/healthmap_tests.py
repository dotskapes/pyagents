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

import os
import unittest
import SimpleHTTPServer
import SocketServer
import multiprocessing as mp

from pyagents.agents import HealthmapAgent

# Allow our testing to actually work
SocketServer.TCPServer.allow_reuse_address = True

class TestHealthmapAgent(unittest.TestCase):

    def setUp(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        cur_path = os.path.join(cur_path, '..')
        self.data_path = os.path.join(cur_path, 'data')
        os.chdir(self.data_path)
        self.port = 9000
        handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", self.port), handler)
        self.server_process = mp.Process(target=httpd.serve_forever)
        self.server_process.start()

    def tearDown(self):
        self.server_process.terminate()
        self.server_process.join()
        del(self.server_process)

    def test_localurl(self):
        json_name = os.path.join(self.data_path, 'test_localurl_output.json')
        settings = {'host': '127.0.0.1',
                    'port': 8888,
                    'path': '/fudd',
                    'source_uri': 'http://localhost:%d/test_localurl.json' % self.port,
                    'mode': 'testing'
                    }
        agent = HealthmapAgent(settings)
        output = agent.update()
        with open(json_name, 'r') as cur_json:
            expected_output = cur_json.read()
            self.assertEqual(output, expected_output)
