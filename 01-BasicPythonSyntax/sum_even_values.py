def sum_even_values(lst):
    result = 0
    for index, element in enumerate(lst):
        if index % 2 == 0:
            result += element
    return result

print sum_even_values([1,2,3])
print sum_even_values([100, 200])


def sum_even_values_alt(lst):
    result = 0
    lst1 = lst[::2]
    for element in lst1:
        result += element
    return result

print sum_even_values_alt([1,2,3])
print sum_even_values_alt([100, 200])
