class Directory(object):

    def __init__(self):
        self._directory = {}

    def add_number(self, name, number):
        self._directory[name] = number

    def remove_number(self, name):
        self._directory.pop(name, None)

    def lookup_number(self, name):
        return self._directory.get(name, '<<unknown>>')

    def print_directory(self):
        for name, number in self._directory.items():
            print '%s: %s' % (name, number)

d = Directory()
d.add_number('Rick', '404.452.5202')
print d.lookup_number('Rick')
d.print_directory()
d.remove_number('Rick')
d.print_directory()

