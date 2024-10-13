# Just a linked list
# Linked list is a tree that doesn't fork

# Full trees either point to Zero nodes or Two nodes
# Perfect tree - any level in a tree that has any nodes that are
# completely filled all the way across
# Complete - Filled from left to right with no gaps

# Every node can only have one parent to be a Tree
# Child nodes can also be parent nodes
# Nodes with no children is called a Leaf

# Binary Search Tree - when the left side contain numbers that
# are less than and the right side contains values that are
# greater than

# Always start by comparing it to the node at the top and compare
# to the child nodes on either side

# BST - Big O
# O(log n) - Divide and Conquer - very efficient
# Could potentially be O(n) if the tree resembles more of a linked list
# where there are little to no forks in the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # can be created with a value or no value

    # with a value
    # def __init__(self, value):
        # new_node = Node(value)
        # self.root = new_node

        # with no value
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while temp:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        # Not necessary
        # if self.root is None:
        #     return False
        temp = self.root
        while temp: # will exit here if self.root is None
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
print(my_tree.contains(27))
print(my_tree.contains(17))