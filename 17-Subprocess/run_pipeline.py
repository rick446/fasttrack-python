from subprocess import Popen, PIPE

sp1 = Popen(['ls', '-laR'], stdout=PIPE)
sp2 = Popen(['wc', '-l'], stdin=sp1.stdout, stdout=PIPE)
stdout, stderr = sp2.communicate()
print '%s lines' % stdout.strip()
