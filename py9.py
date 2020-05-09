
# Finding Intersection 

def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [1,6,3,7,2,8,4,5]
list2 = [1,5,3,7]
print('Custom function:', intersection(list1, list2))
 

"""
Built-in python function for finding intersection
intersection() is only applicable for sets not for others

set is a data structure that is a collection of unique unordered immutable objects.
Unlike lists and tuples, sets do not allow multiple occurrances of the same element.
"""

# example

set1 = set(list1)
set2 = set(list2)

print('set\'s built-in function', set1.intersection(set2))

print('set into list', list(set1.intersection(set2)))