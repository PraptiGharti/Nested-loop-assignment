items = [3, 5, 7, 9, 11, 13]

# Remove item at index 4 (value 11)
element = items.pop(4)

# Add it to the 2nd position (index 1)
items.insert(1, element)

# Add it to the end of the list
items.append(element)

print("Resulting list:", items)


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Identify intersection
intersection = first_set.intersection(second_set)

# Remove these items from first_set
first_set.difference_update(intersection)

print("Updated first_set:", first_set)



first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print("first_set is a subset of second_set.")
    first_set.clear()
elif first_set.issuperset(second_set):
    print("first_set is a superset of second_set.")
    second_set.clear()

print("first_set:", first_set)
print("second_set:", second_set)




month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Extract unique values using a set
unique_values = list(set(month.values()))

print("Unique values list:", unique_values)



sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# Remove duplicates by converting to set, then create a tuple
unique_tuple = tuple(set(sample_list))

print("Tuple:", unique_tuple)
print("Minimum:", min(unique_tuple))
print("Maximum:", max(unique_tuple))




club_A = {"ram", "hari", "shyam"}
club_B = {"ram", "gita", "hari"}

common = club_A.intersection(club_B)

if common:
    print("the following members exist in both groups")
    print(common)
else:
    print("no overlapping members found between groups")




required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}

# Logic: All tasks are done if required_tasks is a subset of completed_tasks
if required_tasks.issubset(completed_tasks):
    print("all tasks done")
else:
    print("some tasks pending")    