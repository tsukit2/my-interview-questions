# Q: What is a heap? And what it can be used for?

# A: A heap is a [binary] tree data structure, usually implemented as array, where the value of the parent
# node is always higher than that of the children (or the smallest, depending on comparison). 
# That means the top value is always the maximum (or minimum) value

# when implemented as array. parent and child positions are calculated as followed
def left(i): return i * 2
def right(i): return i * 2 + 1
def parent(i): return int(i / 2)

# heapify the heap A at position i. The idea is to drift down the element at i down the
# heap by swap its value, when needed, with its children until there is no need to swap anymore
# it has O(h) or O(log n) where h is the tree height an n is the element in the list.
def heapify(A, size, i):
   l = left(i)
   r = right(i)
   largest = l if l < size and A[l] > A[i] else i
   if r < size and A[r] > A[largest]:
      largest = r
   if largest != i:
      A[largest], A[i] = A[i], A[largest]
      heapify(A, size, largest)

# build a heap is easy. The idea is that a given list, we as assume that all elements starting
# from the mid to the end are the leaf of the tree, thus heap of one element. With that assumption,
# then we can work back ward from the lowest-level parent (which is the parent of those leaf nodes)
# and start heapify each one of them. In order word, we gradually float the big values from the
# bottom of the heap to the top
# it has O(n log n) because each call to heapify roughly has O(log n) and there is about n calls
# to it.
def build_heap(A):
   for i in range(int(len(A) / 2), -1, -1):
      heapify(A, len(A), i)


# insert a value into a heap is done by simplying appending it to the end of the list, which
# automatically makes it a child of some note almost at the bottom of the tree. Then the rest
# is just to float it as high as through its parent until the right position is met.
# it has O(log n), which is similar to heapify as it drift the way the opposite way
def insert_heap(A, key):
   A.append(key)
   i = len(A) - 1
   while i > 0 and A[parent(i)] < key:
      A[parent(i)], A[i] = A[i], A[parent(i)]
      i = parent(i)


# to verify whether an array is a heap, we can walk over first half of the area and check,
# for each element, its calculate children are smaller than itself
# it has O(n) as it's just linear search
def verify_heap(A):
   for i in range(int(len(A)/2) + 1):
      if A[left(i)] > A[i] or (right(i) < len(A) and A[right(i)] > A[i]):
         return False
   return True


# heap can be used for sorting. First a heap is built fromthe list. Then since the first element 
# is the largest/smallest, we can just swap it with the end of the list. Then treat the list
# as if it's one element shorter and heapify the list from the top, which will put down the 
# new root value if it's smaller than its new children, then the elements from beginng to the 
# last position to which the maximum was moved to becomes a heap again, ready to provide the next
# largest value
# It has O(n log n) as it call heapify n times.
def heap_sort(l):
   build_heap(l)
   size = len(l)
   for i in range(size-1, 0, -1):
      l[0], l[i] = l[i], l[0]
      size -= 1
      heapify(l,size,0)


# heap can also be used to provide priority queue. This is as simpe as employing the heap insertion
# procedure. When popping out, the maximum value is popped out from the list. Then we grab one
# of the leaf node (the last element in the element) and put it to be the new root. Then heapify
# it to drift it down to its proper position
# it has O(log n) for insert and O(log n) for pop. 
class PriorityQueue:
   def __init__(self):
      self.queue = []

   def insert(self, v):
      insert_heap(self.queue, v)

   def pop(self):
      v = self.queue[0]
      self.queue[0] = self.queue[len(self.queue)-1]
      self.queue.pop()
      heapify(self.queue, len(self.queue), 0)
      return v

   def empty(self):
      return len(self.queue) == 0

   def size(self):
      return len(self.queue)
 


