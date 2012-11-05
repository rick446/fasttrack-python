def print_file_line_numbers(fp):
    import pdb; pdb.set_trace()
    for index, line in enumerate(fp):
        print index + 1, line,

import StringIO

fp = StringIO.StringIO('''The quick
brown fox
jumped over
the lazy dog''')

print_file_line_numbers(fp)

        
