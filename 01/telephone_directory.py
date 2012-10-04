def add_number(directory, name, number):
    directory[name] = number

def remove_number(directory, name):
    del directory[name]

def lookup_number(directory, name):
    return directory[name]

directory = {}
add_number(directory, 'Rick', '404.452.5202')
print lookup_number(directory, 'Rick')
print directory
remove_number(directory, 'Rick')
print directory

def remove_number_alt(directory, name):
    try:
        del directory[name]
    except KeyError:
        pass # ignore KeyError

remove_number_alt(directory, 'Nobody')
print directory
