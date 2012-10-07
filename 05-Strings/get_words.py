def isalpha(ch):
    return ch.isalpha()

def get_words(fp):
    result = []
    for line in fp:
        for word in line.split():
            word = ''.join(filter(isalpha, word.lower()))
            result.append(word)
    return result

text = '''
The quick brown fox jumped over the lazy dog.
The dog was very lazy and the fox was quite quick.
'''

import StringIO
print get_words(StringIO.StringIO(text))
        
def get_words_count(fp):
    result = {}
    for line in fp:
        for word in line.split():
            word = ''.join(filter(isalpha, word.lower()))
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result
    
print get_words_count(StringIO.StringIO(text))


def print_centered_words(words):
    for word in words:
        print word.center(80)

print_centered_words(['The', 'quick', 'brown',  'fox'])
