# Copyright 2019 Arie Bregman
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
import argparse

import cinfo.cli.triage as triage_parser
import cinfo.cli.pull as pull_parser
import cinfo.cli.publish as publish_parser


def create_parser():
    """Returns argument parser"""

    # Top level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser.add_argument('--debug', '-d', action='store_true',
                        dest="debug", help='Turn on debug')

    triage_parser.add_triage_parser(subparsers)
    pull_parser.add_pull_parser(subparsers)
    publish_parser.add_publish_parser(subparsers)

    return parser
