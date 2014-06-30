import StringIO

text = '''
The quick brown fox jumped over the lazy dog.
The dog was very lazy and the fox was quite quick.
'''

def isalpha(ch):
    return ch.isalpha()

def get_words_count(fp):
    result = {}
    for line in fp:
        for word in line.split():
            word = filter(isalpha, word.lower())
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result

print get_words_count(StringIO.StringIO(text))
