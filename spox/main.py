from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from spreadsheet import credential, sheets_api

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1lvtD-DPzNiy8iih9qgCcQoyyLBoCmbFgJ6DRdNR2hMk'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = credential('/Users/kwangin.jung/workspace/study/python/spox/credentials.json')

    # Call the Sheets API
    sheet = sheets_api(creds)
    
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