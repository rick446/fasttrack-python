from cStringIO import StringIO

import codecs

import markdown
from path import path as pathpy
from fabric.api import *
from fabric.contrib.console import confirm

env.user = 'wan_admin'
env.hosts = [ 'arborian.com' ]
env.forward_agent = True

def upload(name):
    with codecs.open(name + '.md', mode='r', encoding='utf-8') as fp:
        lines = fp.readlines()
    text = ''.join(lines)
    html = markdown.markdown(text, [ 'extra', 'codehilite' ])
    sio = StringIO(html.encode('utf-8'))
    put(sio, '~/class.arborian.com/fasttrack-python/%s.html' % name)
    put(StringIO('''<html>
<head>
<link rel="stylesheet" href="/bootstrap/css/bootstrap.css">
</head>
<body>
    <div class="navbar">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="./index.shtml">MongoDB for Developers</a>
        </div>
      </div>
    </div>
<div class="container">
<!--#include file="%s.html" -->
</div>
</body>
</html>''' % name), '~/class.arborian.com/mongodb-devs/%s.shtml' % name)

def upload_html():
    for htmlfile in pathpy('.').glob('*.html'):
        print htmlfile.basename()
        put(htmlfile, '~/class.arborian.com/mongodb-devs/%s' % htmlfile.basename())

