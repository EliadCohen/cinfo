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
import json
import logging
import requests


CALLS = {'get_jobs':
         "/api/json/?tree=jobs[name,lastBuild[result,number,timestamp]]",
         'get_builds': "/job/{}/api/json?tree=allBuilds[number,url]"}
LOG = logging.getLogger(__name__)


class Jenkins(object):
    
    def pull(self, url, jobs=[]):
        data = {'jobs': {},
                'tests': {},
                'job_statuses': {},
                'test_statuses': {}
               }
        for job in jobs:
            LOG.info("  Job: {}".format(job))
            request = requests.get(url + CALLS['get_builds'].format(job), verify=False)
            result_json = json.loads(request.text)
        return result_json
