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
import crayons
import logging
import yaml

LOG = logging.getLogger(__name__)


class Config(object):

    global_config_file = '/etc/cinfo/cinfo.yaml'

    def __init__(self, file=global_config_file):
        self.file = file

    def load(self):
        LOG.info("{}: {}".format(
            crayons.yellow("loading conf"), self.file))
        with open(self.file, 'r') as stream:
            content_yaml = yaml.safe_load(stream)
        return content_yaml
