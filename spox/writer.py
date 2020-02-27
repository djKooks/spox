import json


class Writer:
    """
    TODO:
    """
    def __init__(self):
        pass

    def write_as_json(self, raw, key='en'):
        with open('{}.json'.format(key), 'w', encoding='utf-8') as file:
            json.dump(raw, file, indent='\t')

