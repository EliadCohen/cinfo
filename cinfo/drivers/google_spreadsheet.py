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
import gspread
from gspread.models import Cell
from oauth2client.service_account import ServiceAccountCredentials
import time

import logging

LOG = logging.getLogger(__name__)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cell_colors_by_status = {'SUCCESS': [0, 1, 0],
                         'UNSTABLE': [0.9, 0.9, 0.2],
                         'FAILURE': [1, 0, 0]}


class Google_spreadsheet(object):

    def __init__(self):
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("/etc/google_creds.json", scope)
        self.client = gspread.authorize(self.creds)
    
    def publish(self, data):
        cells_list = []
        sheet = self.client.open("Unified Jobs Triaging")

        # Create worksheets
        try:
            sheet.add_worksheet(title="Per Job", rows="100", cols="20")
            sheet.add_worksheet(title="Per Test", rows="100", cols="20")
            sheet.add_worksheet(title="Per Status", rows="100", cols="20")
        except gspread.exceptions.APIError:
            LOG.debug("Worksheets already exist...skipping")

        ws = sheet.worksheet("Per Job")
        cells_list.append(Cell(1, 1, "This is generated automatically by CInfo. You can edit the spreadsheet and add additional data"))
        i = 2
        for job_name, job_data in data['jobs'].items():
             ws.format("A{0}:H{0}".format(i), {
                 "backgroundColor": {
                     "red": 0.3,
                     "green": 0.8,
                     "blue": 1,
                 }
             })
             i+=1
             cells_list.append(Cell(i, 1, "Job Name"))
             cells_list.append(Cell(i, 2, job_name))
             i+=1
             cells_list.append(Cell(i, 1, "Build Number"))
             cells_list.append(Cell(i, 2, job_data['build_number']))
             i+=1
             cells_list.append(Cell(i, 1, "Build Result"))
             cells_list.append(Cell(i, 2, job_data['result']))
             ws.format("B{0}:B{0}".format(i), {
                 "backgroundColor": {
                     "red": cell_colors_by_status[job_data['result']][0],
                     "green": cell_colors_by_status[job_data['result']][1],
                     "blue": cell_colors_by_status[job_data['result']][2],
                 }
             })
             i+=1
             if job_data['result'] == "UNSTABLE":
                 cells_list.append(Cell(i, 1, "Tests Results"))
                 ws.format("A{0}:C{0}".format(i), {
                     "backgroundColor": {
                         "red": 0.9,
                         "green": 0.8,
                         "blue": 0.8
                     }
                 })
                 i+=1
                 cells_list.append(Cell(i, 1, 'className'))
                 cells_list.append(Cell(i, 2, 'name'))
                 cells_list.append(Cell(i, 3, 'status'))
                 cells_list.append(Cell(i, 4, 'duration'))
                 cells_list.append(Cell(i, 5, 'skipped'))
                 cells_list.append(Cell(i, 6, 'skippedMessage'))
                 i+=1
                 for test in job_data['tests']:
                     if test['status'] != "SKIPPED" and test['status'] != "PASSED":
                         cells_list.append(Cell(i, 1, test['className']))
                         cells_list.append(Cell(i, 2, test['name']))
                         cells_list.append(Cell(i, 3, test['status']))
                         cells_list.append(Cell(i, 4, test['duration']))
                         cells_list.append(Cell(i, 5, test['skipped']))
                         cells_list.append(Cell(i, 6, test['skippedMessage']))
                         i+=1
        ws.update_cells(cells_list)
