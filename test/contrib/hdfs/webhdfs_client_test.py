# -*- coding: utf-8 -*-
#
# Copyright 2015 VNG Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest

from hdfs import InsecureClient
from hdfs.ext.kerberos import KerberosClient
from nose.plugins.attrib import attr

from helpers import with_config
from contrib.hdfs_test import HdfsTargetTestMixin
from luigi.contrib.hdfs import WebHdfsClient


@attr('apache')
class TestWebHdfsClient(unittest.TestCase):

    @with_config({'webhdfs': {'client_type': 'insecure'}})
    def test_insecure_client_type(self):
        client = WebHdfsClient(host='localhost').client
        self.assertIsInstance(client, InsecureClient)

    @with_config({'webhdfs': {'client_type': 'kerberos'}})
    def test_kerberos_client_type(self):
        client = WebHdfsClient(host='localhost').client
        self.assertIsInstance(client, KerberosClient)
