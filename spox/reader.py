

class Reader:
    """
    TODO:
    """
    value = []
    key_range_length = 1
    lang_type = {}

    def __init__(self, sheet):
        if 'values' in sheet:
            self.value = sheet['values']

            for idx, val in enumerate(self.value[0]):
                if idx == 0:
                    if val != 'key':
                        raise ValueError('Cannot find key')
                else:
                    if not val:
                        self.key_range_length += 1
                    else:
                        self.lang_type[val] = idx
        else:
            raise ValueError('Key "value" not exists in sheet')

    def get_column_info(self):
        return {
            'key_range_length': self.key_range_length,
            'lang_type': self.lang_type.keys()
        }

    def get_lang_by_column(self, lang_key):
        key = self.lang_type[lang_key]
        new_list = [list[key] for idx, list in enumerate(self.value) if idx != 0]
        print(new_list)
        pass
