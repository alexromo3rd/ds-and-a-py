# Dictionaries - Built in Hash Tables in Python
# Has a big O of O(1) to place a key/value pair
# or to lookup something in a Hash Table
# Key/Value pairs
# Perform Hash on the key - returns key/value pair back as well
# as an address where the key/value pair is stored
# One way - put key through hash to get the value but 
# you can't put the value through hash to get key
# It is Deterministic, meaning for a particular hash function
# every time you put "nails" in you expect to get the value
# 2 back every time

# Collisions - happen whe you put a key/value pair at an address
# where there is already a key/value pair

# Separate Chaining - storing two or more key/value pairs at the
# same address

# Linear Probing  - looks for an empty spot to store the key/value
# pair if the address is already taken. This is a form of open addressing.

# You should always have a prime number of addresses because a prime number
# increases the amount of randomness for how the key/value pairs are going
# to be distributed through the hash table which reduces collisions

class HashTable:
    def __init__(self, size = 7):
        # creates a list of 7 items, all are None value
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 50)
# my_hash_table.print_table()

# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))

print(my_hash_table.keys())