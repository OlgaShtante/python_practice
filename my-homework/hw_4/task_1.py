# define three lists
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
list_3 = ["%", "$", "@"]

# zip lists
zipped_values = zip(list_1, list_2, list_3)

# print new tuples
for tuple_value in zipped_values:
    print(tuple_value)