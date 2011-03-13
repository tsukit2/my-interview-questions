# Q: What is binary tree. How to perform different operations on it

# A: A binary tree is a tree whose each node can have at most 2 children. The left child node 
# has value less than the parent, while the right node has the greater. The operations on the
# tree are subject to the height of the tree. If the tree is imbalanced, it would look like 
# just a linked list


class BinaryTree:
   def __init__(self, v):
      self.value = v
      self.parent = None
      self.left = None
      self.right = None

   # to insert, compare the inserted value with the current node. If value is equals to or greater than, 
   # move down to its right child, if any, and attemp to insert there. If it's less than, move to
   # the left child. If no child, stop there. Then insert the node either at left or right
   def insert(self, t):
      node = child = self
      while child != None:
         node = child
         if t.value < node.value:
            child = node.left
         else:
            child = node.right

      if t.value < node.value:
         node.left = t
      else:
         node.right = t
      t.parent = node

   # to delete, if the node doesn't have any children, just delete it and empty out the poiter
   # in parent. If it does have one child (either left or right), pull it up and make the parent
   # point to it. If it has two children, find its successor (could be way down below). Then
   # recursively delete the successor and use its value to replace the node being deleted.
   def delete(self):
      # case 1: no children. we just remove it from parent
      if self.left == None and self.right == None:
         if self.parent:
            if self.parent.value < self.value:
               self.parent.right = None
            else:
               self.parent.left = None
      # case 2.1: only has left child, connect left child to parent
      elif self.right == None:
         if self.parent:
            if self.parent.value < self.value:
               self.parent.right = self.left
            else:
               self.parent.left = self.left
      # case 2.2: only has right child, connect right child to parent
      elif self.left == None:
         if self.parent:
            if self.parent.value < self.value:
               self.parent.right = self.right
            else:
               self.parent.left = self.right
      # case 3: has both children, recursively splice off its successor and use its value
      else:
         succ = self.successor()
         succ.delete()
         self.value = succ.value

   # to find minimum, just go all the way left 
   def minimum(self):
      node = self
      while node.left:
         node = node.left
      return node
     
   # to find maximum, just go all the way right
   def maximum(self):
      node = self
      while node.right:
         node = node.right
      return node

   # to find successor, if it has the right child, find the minimum from the left child tree
   # otherwise, keep going up to the parent in the chain whose value is *greater* than the current
   # node in the chain
   def successor(self):
      if self.right:
         return self.right.minimum()

      node = self
      parent = self.parent
      while parent and parent.value < node.value:
         node = parent
         parent = parent.parent
      return parent

   # to find a value n, check if the current node's value equals to it. If not, see if n is
   # greater than the node, if so, move on to the right child node, or left child if less than
   def find(self, n):
      node = self
      while node and node.value != n:
         if n > node.value:
            node = node.right
         else:
            node = node.left
      return node

sampletree = BinaryTree(15)
for n in [5, 16, 3, 12, 20, 10, 13, 18, 23, 7, 6]:
   sampletree.insert(BinaryTree(n))

            



      
      
