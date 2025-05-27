my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [my_list[num] for num in range (0, len(my_list), 3)]
print(new_list)