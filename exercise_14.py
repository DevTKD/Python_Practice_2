empty_list = []
empty_list.append(10)
empty_list.append(25)
empty_list.append(30)
empty_list.append(45)
empty_list.append(90)
print(empty_list)
empty_list.append("ab")
empty_list.append("cd")
empty_list.append("ef")
print(empty_list)

#Optimized code alternative
# Start with an empty list
empty_list = []

# Add numbers to the list
empty_list.extend([10, 25, 30, 45, 90])
print(empty_list)

# Add strings to the list
empty_list.extend(["ab", "cd", "ef"])
print(empty_list)