import re


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        if (re.match(self.regex, value)):
            return value
        else:
            return '2016-01-01'

    def to_url(self, value):
        return value.__str__()
