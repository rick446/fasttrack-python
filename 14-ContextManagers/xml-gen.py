class node(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print '<%s>' % self.name

    def __exit__(self, ex_type, ex_value, ex_tb):
        print '</%s>' % self.name

with node('html'):
    with node('body'):
        with node('h1'):
             print 'Page Title'

