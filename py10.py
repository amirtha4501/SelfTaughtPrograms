my_list = [1, 2, 1, 4, 5, 4, 2, 6, 6]

def non_duplicates(my_list):
    count = {}
    for i in my_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for k, v in count.items():
        if v == 1:
            print(k)

non_duplicates(my_list)



# return duplicates

def return_duplicates(a_list):
    dups = []
    a_set = set()
    for item in a_list:
        len_1 = len(a_set)
        a_set.add(item)
        len_2 = len(a_set)

        if len_1 == len_2:
            dups.append(item)
    return dups

a_list = [1, 3, 4, 6, 3, 5, 7, 9, 1]
print(return_duplicates(a_list))