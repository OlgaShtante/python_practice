list = [1,2,5]
is_sorted = all(list[i] <= list[i + 1] for i in range(len(list) - 1))