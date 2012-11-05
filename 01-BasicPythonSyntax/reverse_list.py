def reverse_list(lst):
    return lst[::-1]

def reverse_list2(lst):
    lst.reverse()
    return lst

def reverse_list3(lst):
    lst = list(reversed(lst))
    return lst

print reverse_list([1,2,3])
print reverse_list2([1,2,3])
print reverse_list3([1,2,3])

