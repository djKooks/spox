from __future__ import print_function

from reader import Reader
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
    print('start main')
    lang_list = get_range(env['lang'])
    sheet = sheets_api(credential(env['credential_file_path']))

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    print(result)

    reader = Reader(result)
    # print(reader.get_column_info())
    # print(reader.get_lang_by_column('ko'))


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
