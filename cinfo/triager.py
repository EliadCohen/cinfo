# Copyright 2021 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import logging

from cinfo.config import Config

LOG = logging.getLogger(__name__)


class Triager(object):

    def __init__(self, config_file):
        self.config_file = config_file

    def load_config(self):
        self.config = Config(file=self.config_file)
        self.config.load()

    def pull(self):
        pass

    def publish(self):
        pass

    def run(self):
        self.load_config()
        self.pull()
        self.publish()
