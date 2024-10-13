# LIFO - Last In, First Out
# Can use a linked list to create a stack
# Linked list is O(1) if items are removed from end only
# None must be pointing down with last node at the bottom of the stack
# Instead of Head and Tail, you have Top and Bottom for Stack (Bottom not needed since adding/removing are done at the Top)
# Items are added and removed from Top of the stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        # self.bottom = new_node # can be removed (optional)
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp

my_stack = Stack(2)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()