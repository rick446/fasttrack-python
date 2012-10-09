import os
import subprocess

for filename in os.listdir('.'):
    print subprocess.check_output(['stat', filename])
