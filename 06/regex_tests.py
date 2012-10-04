import re
re_integer = re.compile(r'(\d+)')

def find_integers(fp):
    result = []
    for line in fp:
        for match in re_integer.finditer(line):
            result.append(int(match.group(1)))
    return result

text = '''The 42nd number in a list of integers starting at
0 is actually 41. It's a surprising result, but one that
computer scientists have dealt with since the days of IBM mainframes.'''

import StringIO
print 'Integers:', find_integers(StringIO.StringIO(text))

re_capword = re.compile(r'(?:\W|^)([A-Z]\w*)')
def find_capwords(fp):
    result = []
    for line in fp:
        for match in re_capword.finditer(line):
            result.append(match.group(1))
    return result
    
print 'Capwords:', find_capwords(StringIO.StringIO(text))

re_br = re.compile(r'<br>')
def bad_html_to_xhtml(fp):
    result = []
    for line in fp:
        new_line = re_br.sub('<br/>', line)
        result.append(new_line)
    return ''.join(result)

print 'Bad html to xhtml:', bad_html_to_xhtml(StringIO.StringIO('''
<div>
This works ok
<br>
</div>'''))
