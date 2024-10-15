# Two lists are given
# 1, 3, 5
# 2, 4, 5

# Big O is O(n^2)
# Naive approach would be to create a nested for loop
# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False

# list1 = [1, 3, 5]
# list2 = [2, 4, 5]

# print(item_in_common(list1, list2))
 
# Second approach is to use a dictionary
# Big O is O(n)

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))