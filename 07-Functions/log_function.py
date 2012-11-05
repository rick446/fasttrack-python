def log(format, *args, **kwargs):
    if args:
        print format % args
    else:
        print format % kwargs

log('The pair is (%r,%r)', 1, 2)
log('The value of a is %(a)r', a='foo')
log('The value of a is %(a)r', **{'a': 'foo'})

log('This does not have any arguments')
