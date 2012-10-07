from contextlib import contextmanager

@contextmanager
def node(name):
    print '<%s>' % name
    yield
    print '</%s>' % name

with node('html'):
    with node('body'):
        with node('h1'):
             print 'Page Title'
        
