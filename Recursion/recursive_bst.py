# Recursive Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # def insert(self, value):
    #         new_node = Node(value)

    #         if self.root is None:
    #             self.root = new_node
    #             return True

    #         temp = self.root
    #         while temp:
    #             if new_node.value == temp.value:
    #                 return False
    #             if new_node.value < temp.value:
    #                 if temp.left is None:
    #                     temp.left = new_node
    #                     return True
    #                 temp = temp.left
    #             else:
    #                 if temp.right is None:
    #                     temp.right = new_node
    #                     return True
    #                 temp = temp.right

    # Recursive Insert
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node  
    
    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value) 


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        current_node = self.root
        self.__delete_node(current_node, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
# my_tree.r_insert(47)
# my_tree.r_insert(21)
# my_tree.r_insert(76)
# my_tree.r_insert(18)
# my_tree.r_insert(27)
# my_tree.r_insert(52)
# my_tree.r_insert(82)


# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.right))
print('root:', my_tree.root.value)
print('root.left:', my_tree.root.left.value)
print('root.right:', my_tree.root.right.value)

my_tree.delete_node(2)

print('root:', my_tree.root.value)
print('root.left:', my_tree.root.left.value)
print('root.right:', my_tree.root.right)
# print('BST Contains 27:')
# print(my_tree.r_contains(27))

# print('BST Contains 17:')
# print(my_tree.r_contains(17))