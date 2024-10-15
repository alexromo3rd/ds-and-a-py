# Similar to a BST, though the numbers are not distributed the same way
# Priority Queue - Insert and Remove will always be O(log n)
# Hightest value will always be at the top
# It is a complete tree - must be filled from left to right on each level
# with no gaps
# Can contain duplicates
# Max Heap - highest value at the top
# Can also have a Min Heap where minimum value is at the top
# No particular order, just that all descendants need to be less
# than or equal to the item at the top

# Not good for searching
# Best for keeping largest item at the top and be able to quickly remove it

# Stored in a list
# Won't create a Node class
# Only stores integers
# Heaps can start with index of 0 or 1
# Contiguous range of numbers


# When index starts at 1
# To find left child = 2 * parent_index
# To find right child = 2 * parent_index + 1

# Equation for finding a parent of a particular node
# To find left child = index / 2
# To find right child = index / 2, drop the decimal value

# Insert value in the next open spot first to keep the heap complete
# Then compare against parent and swap if it's greater than parent

class MaxHeap:
    def __init__(self):
        self.heap = []

    # For when index starts at 0
    # Different calculation from above
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        
    def remove(self):
        # Always remove the top item only for Min or Max heap
        # Always make the tree complete
        # Move last item to the top position
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

print(my_heap.heap)

my_heap.remove()

print(my_heap.heap)

my_heap.remove()

print(my_heap.heap)