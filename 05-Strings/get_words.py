import StringIO

text = '''
The quick brown fox jumped over the lazy dog.
The dog was very lazy and the fox was quite quick.
'''

def isalpha(ch):
    return ch.isalpha()

def get_words(fp):
    result = []
    for line in fp:
        for word in line.split():
            word = word.lower()
            word = filter(isalpha, word)
            result.append(word)
    return result

print get_words(StringIO.StringIO(text))
