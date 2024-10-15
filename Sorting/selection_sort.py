# Looks at first item and keeps track of index where the min value is
# Store index in min_index variable
# For loop starts at next item over
# Compares item at first loop index to item at min_index and if
# it is, it updates the min_index to the lower value and moves through
# to the end of the loop looking for lower values and storing their index
# if they are less than the previous min_index value
# at the end of that loop, it swaps the value at min_index with the first
# item at index 0, then moves to the next item, etc

# Big O - O(n^2)
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


my_list = [4, 2, 6, 5, 1, 3]

print(selection_sort(my_list))