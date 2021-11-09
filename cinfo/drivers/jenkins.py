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
         'get_builds': "/job/{}/api/json?tree=allBuilds[number,url,result,actions[causes]]",
         'get_tests': "/job/{}/{}/testReport/api/json"
        }
LOG = logging.getLogger(__name__)


class Jenkins(object):
    
    def pull(self, url, jobs=[]):
        data = {'jobs': {},
                'tests': {},
                'build_statuses': {'SUCCESS': [], 'FAILURE': [],
                                   'UNSTABLE': [], 'ABORTED': []},
               }
        for job in jobs:
            LOG.info("  Job: {}".format(job))
            request = requests.get(url + CALLS['get_builds'].format(job), verify=False)
            result_json = json.loads(request.text)
            data['jobs'][job] = {'build_number': -1} 
            for build in result_json['allBuilds']:
                if "causes" in build['actions'][0] and "GerritCause" in build['actions'][0]['causes'][0]['_class']:
                    pass
                elif "causes" in build['actions'][0] and "BuildUpstreamCause" in build['actions'][0]['causes'][0]['_class']:
                    if build['number'] > data['jobs'][job]['build_number']:
                        build_data = {'build_number': build['number'], 'result': build['result'],
                                      'url': build['url'], 'job': job, 'tests': []}
                else:
                    pass
            if build_data['result'] == 'UNSTABLE':
                tests_request = requests.get(url + CALLS['get_tests'].format(
                    job,build_data['build_number']), verify=False)
                build_tests_json = json.loads(tests_request.text)
                build_data['tests_duration'] = build_tests_json['duration']
                build_data['tests_fail_count'] = build_tests_json['failCount']
                build_data['tests_pass_count'] = build_tests_json['passCount']
                build_data['tests_skip_count'] = build_tests_json['skipCount']
                test_data = {}
                for test_suite in build_tests_json['suites']:
                    for case in test_suite['cases']:
                        tests_data = {'age': case['age'], "className": case['className'],
                                      'skipped': case['skipped'], 'skippedMessage': case['skippedMessage'],
                                      'name': case['name'], 'status': case['status'],
                                      'duration': case['duration']}
                        build_data['tests'].append(tests_data)
                        if case['status'] == "FAILED":
                            if case['name'] not in data['tests']:
                                data['tests'][case['name']] = {'jobs': [job], 'name': case['name']}
                            else:
                                data['tests'][case['name']]['jobs'].append(job)

            data['jobs'][job] = build_data
            data['build_statuses'][build_data['result']].append(build_data)
        return data
