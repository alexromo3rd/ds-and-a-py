# Bubble Sort - start with first item in the list, then move to 2nd
# compare 2nd to the third, then third to fourth, etc.
# Swap items and move the largest item to the right

# Big O - Time Complexity O(n^2)
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

my_list = [4, 2, 6, 5, 1, 3]

print(bubble_sort(my_list))