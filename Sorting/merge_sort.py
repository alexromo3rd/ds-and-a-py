# If you have two separate lists that are already sorted, then it's
# easy to combine them to make a single sorted list

# Merge is a helper function
# Takes two sorted lists, takes values, and puts them into a new
# combined list

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

# Big O - Space Complexity - O(n)
# Big O - Time Complexity - O(log n) to break them down
# Big O - Time Complexity to merge them back together is O(n)
# Big O - Time Complexity for entire process is O(n log n)
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2) # drops decimal place for odd number lists
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

# list1 = [3,1,4,2]
# list2 = [2,4,5,6]

# print(merge(list1, list2))

original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)

print('Original List:', original_list)
print('\norted List:', sorted_list)