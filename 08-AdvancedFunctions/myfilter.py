def myfilter(function, sequence):
    result = []
    for item in sequence:
        if function(item):
            result.append(item)
    return result

print myfilter(lambda x: x%2==0, range(10))
print myfilter(lambda x: x%2==1, range(10))

def myfilter(function, sequence1, sequence2):
    result = []
    for item1, item2 in zip(sequence1, sequence2):
        if function(item1, item2):
            result.append((item1, item2))
    return result

def myfilter(function, *sequences):
    result = []
    for items in zip(*sequences):
        if function(*items):
            result.append(items)
    return result

