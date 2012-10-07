def log(format, *args, **kwargs):
    if args:
        print format % args
    elif kwargs:
        print format % kwargs
    else:
        print format

log('The pair is (%r,%r)', 1, 2)
log('The value of a is %(a)r', a='foo')
