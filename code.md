# Code Examples 

<!-- [[[cog
from path import path
import cog
import os

for dirname in path('.').glob('??-*/'):
    if dirname.endswith('_files/'): continue
    cog.outl('## %s\n' % dirname)
    for fn in dirname.listdir():
        if fn.endswith('.pyc'): continue
        cog.outl('- %s' % fn)
    cog.outl('')
]]]-->
<!-- [[[end]]] -->
