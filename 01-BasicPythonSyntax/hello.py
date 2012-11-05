#!/usr/bin/env python
def sayhello(name):
    print 'Hello, ' + name

def sayhello2(name):
    print 'Hello,', name # using ',' inserts a space

def sayhello3(name):
    print 'Hello,',  # no \n at end
    print name

sayhello('VMware')
sayhello2('VMware')
sayhello3('VMware')
