
# list comprehension last digit

inp_str = "Buy 1 get 2 free"
new_list = [c for c in inp_str if c.isdigit()][-1]
print(new_list)

# list comprehension syntax
""" new_line = [expression(i) for i in input_list if filter(i)]"""

# list comprehension exercise

ip_list = [1, 7, 5, 3, 2]

new_list = [i * 7 for i in ip_list]

print(new_list)