def ascii2str(lst):
    s = ''
    characters = map(chr, lst)
    for ch in characters:
        s += ch
    return s

print ascii2str([86, 77, 87, 97, 114, 101])

def ascii2str_alt(lst):
    characters = map(chr, lst)
    return ''.join(characters)

print ascii2str_alt([86, 77, 87, 97, 114, 101])
