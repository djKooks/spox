

class Reader:

    value = {}
    def __init__(self, sheet):
        if 'values' in sheet:
            self.value = sheet['values']
        else:
            raise ValueError('Key "value" not exists in sheet')

    def get_column_info(self):
        key_range_length = 1
        lang_type = []

        for idx, val in enumerate(self.value[0]):
            if idx == 0:
                if val != 'key':
                    raise ValueError('Cannot find key')
            else:
                if not val:
                    key_range_length += 1
                else:
                    lang_type.append(val)

        return {
            'key_range_length': key_range_length,
            'lang_type': lang_type
        }

    def get_lang_by_column(self):
        pass
