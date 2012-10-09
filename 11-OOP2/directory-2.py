class Directory(object):

    def __init__(self):
        self._directory = {}

    def add_number(self, name, number):
        self._directory[name] = number

    def remove_number(self, name):
        del self._directory[name]

    def lookup_number(self, name):
        return self._directory[name]

    def __getitem__(self, name):
        return self.lookup_number(name)

    def __setitem__(self, name, number):
        self.add_number(name, number)

    def __delitem__(self, name):
        self.remove_number(name)

    def __repr__(self):
        l = ['<Directory>']
        for name, number in self._directory.items():
            l.append('    %s: %s' % (name, number))
        l.append('</Directory>')
        return '\n'.join(l)

class DefaultDirectory(Directory):

    def __init__(self, default_number):
        self._default = default_number
        super(DefaultDirectory, self).__init__()

    def lookup_number(self, name):
        try:
            return super(DefaultDirectory, self).lookup_number(name)
        except KeyError:
            return self._default

    def remove_number(self, name):
        try:
            super(DefaultDirectory, self).remove_number(name)
        except KeyError:
            print (
                'Would have raised an exception deleting %s'
                % name)
            pass

    def __repr__(self):
        l = ['<DefaultDirectory(%r)>' % self._default]
        for name, number in self._directory.items():
            l.append('    %s: %s' % (name, number))
        l.append('</DefaultDirectory>')
        return '\n'.join(l)

d = Directory()
d['Rick'] = '404.452.5202'
print "Rick's number is", d['Rick']
print d
del d['Rick']
print d

dd = DefaultDirectory('default')
dd['Rick'] = '404.452.5202'
print 'Rick: %s' % dd['Rick']
print 'Stuart: %s' % dd['Stuart']
print dd
del dd['Stuart']
