def sum_values(lst):
    result = 0
    for element in lst:
        result += element
    return result

print sum_values([1,2,3])
print sum_values([100, 200])
