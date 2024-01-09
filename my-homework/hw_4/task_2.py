# define a list
current_list =  ["apple", "banana", "cherry"]

# revert every string in the list
new_list = list(map(lambda n: n[::-1], current_list))

# print reverted strings
for reverted_string in new_list:
    print(reverted_string)