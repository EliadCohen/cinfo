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
import os

from cinfo.triager import Triager

LOG = logging.getLogger(__name__)


def add_triage_parser(subparsers):
    """The parser for sub command 'triage'."""
    run_parser = subparsers.add_parser("triage")
    run_parser.set_defaults(func=main)
    run_parser.add_argument('--config', dest="config_file",
                            default=os.path.join(os.path.expanduser("~"),
                                                 '.cinfo/cinfo.yaml'),
                            help='the path of cinfo configuration')
    run_parser.add_argument('--source', dest="source",
                            help='name of the source to use')


def main(args):
    """Runner main entry."""
    # TODO(abregman): do actually something with debug
    del args.debug
    del args.func
    triager = Triager(config_file=args.config_file,
                      source=args.source)
    triager.run()
