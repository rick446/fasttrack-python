def print_file(fp):
    for line in fp:
        print line[:-1]

fp = open('/etc/hosts')
print_file(fp)
fp.close()

def print_file_line_numbers(fp):
    for index, line in enumerate(fp):
        print index + 1, line[:-1]

fp = open('/etc/hosts')
print_file_line_numbers(fp)
fp.close()
