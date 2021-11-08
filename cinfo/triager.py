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
import sys

from cinfo.config import Config
from cinfo.exceptions import usage as usage_exc

LOG = logging.getLogger(__name__)


class Triager(object):

    def __init__(self, config_file, source=None):
        self.config_file = config_file
        self.source=source

    def load_config(self):
        self.config = Config(file=self.config_file)
        self.config.load()
        self.sources = self.config.data['sources']
        self.targets = self.config.data['targets']

    def pull(self):
        pass

    def publish(self):
        pass

    def validate(self):
        if len(self.sources.keys()) > 1 and not self.source:
            LOG.error(usage_exc.multiple_sources())
            sys.exit(2)

    def run(self):
        self.load_config()
        self.validate()
        self.pull()
        self.publish()
