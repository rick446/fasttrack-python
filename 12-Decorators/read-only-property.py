class MyClass(object):

    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        return self._a

x = MyClass('avalue')
print x.a
x.a = 'bvalue'
