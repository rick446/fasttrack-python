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
        print 'Begin directory'
        print self._directory
        for name, number in self._directory.items():
            print '    %s: %s' % (name, number)
        print 'End directory'

d = Directory()
d.add_number('Rick', '404.452.5202')
print 'Rick has number', d.lookup_number('Rick')
d.print_directory()
print
d.remove_number('Rick')
d.print_directory()
print
print 'Rick has number', d.lookup_number('Rick')
print
d.remove_number('Rick')

