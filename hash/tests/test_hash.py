#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import logging
import unittest

from pathlib import Path

from stoq import RequestMeta, Stoq, Payload
from stoq.data_classes import WorkerResponse


class TestCore(unittest.TestCase):
    def setUp(self) -> None:
        self.plugin_name = 'hash'
        self.base_dir = Path(os.path.realpath(__file__)).parent
        self.data_dir = os.path.join(self.base_dir, 'data')
        self.plugin_dir = os.path.join(self.base_dir.parent, self.plugin_name)
        self.generic_data = b'This is a payload to hash'

    def tearDown(self) -> None:
        pass

    def test_scan(self) -> None:
        s = Stoq(plugin_dir_list=[self.plugin_dir])
        plugin = s.load_plugin(self.plugin_name)
        payload = Payload(self.generic_data)
        response = plugin.scan(payload, RequestMeta())
        self.assertIsInstance(response, WorkerResponse)
        self.assertEqual('cfe671457bc475ef2f51cf12b1457475', response.results['md5'])
        self.assertEqual(
            'f610f70b1464d97f7897fefd6420ffc904df5e4f', response.results['sha1']
        )
        self.assertEqual(
            '2fa284e62b11fea1226b35cdd726a7a56090853ed135240665ceb3939f631af7',
            response.results['sha256'],
        )
