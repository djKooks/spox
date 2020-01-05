from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from env import read_env
from spreadsheet import get_range, credential, sheets_api

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1lvtD-DPzNiy8iih9qgCcQoyyLBoCmbFgJ6DRdNR2hMk'

# Define Range
# <sheet name>!<left-top cell>:<right-bottom cell>
SAMPLE_RANGE_NAME = 'sheet-1!A1:E5'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    env = read_env()
    creds = credential(env['credential_file_path'])
    get_range(env['lang'])
    # Call the Sheets API
    sheet = sheets_api(creds)
    
    # sheet_range = 

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    print(result)
    '''
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    '''

if __name__ == '__main__':
    main()