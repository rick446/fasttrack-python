def sum_even_values(lst):
    result = 0
    lst1 = lst[::2]
    for element in lst1:
        result += element
    return result

print sum_even_values([1,2,3])
print sum_even_values([100, 200])
