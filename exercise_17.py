list_1 = [9,8,7,14,3,2,"a","p","hello","b"]
list_2 = ["b", 1,9,9.2,6,3,9,"p"]

list_3 = []

for item1 in list_1:
    for item2 in list_2:
        if item1 == item2:
            list_3.append(item1)
            break
print(list_3)