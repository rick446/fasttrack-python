class with_file(object):

    def __init__(self, *open_args):
        self._open_args = open_args

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            fp = open(*self._open_args)
            try:
                return function(fp, *args, **kwargs)
            finally:
                fp.close()
        return wrapper

def with_file_alt(*open_args):
    def decorator(function):
        def wrapper(*args, **kwargs):
            fp = open(*open_args)
            try:
                return function(fp, *args, **kwargs)
            finally:
                fp.close()
        return wrapper
    return decorator

@with_file('/etc/hosts')
def print_file(fp):
    for i, line in enumerate(fp):
        print '%.4d: %s' % (i+1, line.rstrip())

@with_file_alt('/etc/hosts')
def print_file_2(fp):
    for i, line in enumerate(fp):
        print '%.4d: %s' % (i+1, line.rstrip())


print_file()
print_file_2()
