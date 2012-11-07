from contextlib import contextmanager

# class contextmanager(object):

#     def __init__(self, generator):
#         self._generator = generator

#     def __enter__(self):
#         return self._generator.next()

#     def __exit__(self, ex_type, ex_value, ex_tb):
#         try:
#             self._generator.next()
#         except StopIteration:
#             return

@contextmanager
def node(name):
    print '<%s>' % name
    yield None
    print '</%s>' % name

htmlnode = node('html')
bodynode = node('body')
h1node = node('h1')

with htmlnode:
    with bodynode:
        with h1node:
            print 'Page title'

with node('html'):
    with node('body'):
        with node('h1'):
             print 'Page Title'
        
