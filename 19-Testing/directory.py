class Directory(object):

    def __init__(self):
        self._directory = {}

    def add_number(self, name, number):
        self._directory[name] = number

    def remove_number(self, name):
        del self._directory[name]

    def lookup_number(self, name):
        return self._directory[name]

    def __repr__(self):
        l = ['<Directory>']
        for name, number in self._directory.items():
            l.append('    %s: %s' % (name, number))
        l.append('</Directory>')
        return '\n'.join(l)

