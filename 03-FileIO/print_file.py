def print_file(fp):
    for line in fp:
        print line.rstrip() # remove trailing whitespace

fp = open('/etc/hosts')
print_file(fp)
fp.close()

def print_file_line_numbers(fp):
    for index, line in enumerate(fp):
        print index + 1, line.rstrip()

fp = open('/etc/hosts')
print_file_line_numbers(fp)
fp.close()

        
