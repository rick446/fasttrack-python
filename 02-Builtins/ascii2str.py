def ascii2str(lst):
    s = ''
    characters = map(chr, lst)
    for ch in characters:
        s += ch
    return s

print ascii2str([80, 121, 116, 104, 111, 110, 32, 82, 117, 108, 101, 122])

def ascii2str_alt(lst):
    characters = map(chr, lst)
    return ''.join(characters)

print ascii2str_alt([82, 117, 98, 121, 32, 68, 114, 111, 111, 108, 122])
