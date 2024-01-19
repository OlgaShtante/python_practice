input_list = [3, 5]

input_list.sort()

first_str = input_list[0]
last_str = input_list[-1]

common_prefix = ""
for i in range(len(first_str)):
    if first_str[i] == last_str[i]:
        common_prefix += first_str[i]
    else:
        break

#return common_prefix
