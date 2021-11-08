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


def general_usage():
    """Returns general usage string."""
    message = """
Choose one of the following cinfo actions: {}
Usage Examples:

    Full triage (pull & publish):
    $ {}

    Pull data only:
    $ {}

    Publish local data:
    $ {}

""".format(crayons.red("triage, pull, publish"),
           crayons.yellow('cinfo triage'),
           crayons.yellow('cinfo pull'),
           crayons.yellow("cinfo publish"))
    return message


def multiple_sources():
    """Returns multiple sources exception."""
    message = """
There is more than one source defined...can't decide which one to use.
Please specify a single source with {}
""".format(crayons.red("--source NAME"))
    return message
