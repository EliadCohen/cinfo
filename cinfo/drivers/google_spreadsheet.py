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

import logging

LOG = logging.getLogger(__name__)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


class Google_spreadsheet(object):

    def __init__(self):
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("/etc/google_creds.json", scope)
        self.client = gspread.authorize(self.creds)
    
    def publish(self, data):
        sheet = self.client.open("Unified Jobs Triaging")

        # Create worksheets
        try:
            sheet.add_worksheet(title="Per Job", rows="100", cols="20")
            sheet.add_worksheet(title="Per Test", rows="100", cols="20")
            sheet.add_worksheet(title="Per Status", rows="100", cols="20")
        except gspread.exceptions.APIError:
            LOG.debug("Worksheets already exist...skipping")

        ws = sheet.worksheet("Per Job")
        import pdb;pdb.set_trace()
        for job in data['jobs']:
             ws.update_cell(i, 1, 'Bingo!')


        cells_list = []
        cells_list.append(Cell(row=1, col=1 , value="This spreadsheet is auto-generated by cinfo (github.com/bregman-arie/cinfo). PLEASE DON'T EDIT MANUALLY :)"))
        general_sheet.update_cells(cells_list)