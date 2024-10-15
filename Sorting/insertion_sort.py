# Always starts with 2nd item in the list
# Compare with item before it and swaps if it's less than prev item

# Big O - O(n^2) unless list is already sorted or mostly sorted, then
# Big O is O(n)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


my_list = [4, 2, 6, 5, 1, 3]

print(insertion_sort(my_list))