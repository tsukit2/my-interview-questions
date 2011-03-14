# Q: What is AVL tree and why we need it. 

# A: AVL tree is an auto-balanced binary tree. It's better
# than the normal binary tree because it keeps autobalancing itself so that the search can be
# done still at O(log n) time, preventing becoming linear. Insertion and deletion of the AVL
# tree us worse than regular binary tree because balancing act needs to be done. The individual
# balancing is done in O(1) - finite steps are defined. It needs to be done O(h) times. So roughly
# both operations would still be O(h).
#

from binarytree import BinaryTree

class AVLTree(BinaryTree):

   # insertion of AVL tree is like the binary tree. The only thing to do is to just balancing
   # the parent.
   def insert(self, t):
      BinaryTree.insert(self, t)
      if t.parent:
         t.parent.balance_tree()

   # deletion of AVL tree is also like insertion in that the parent of the replacement need
   # need to be rebalanced
   def delete(self):
      parent = self.parent
      BinaryTree.delete(self)
      parent.balance_tree()

   # to balance the tree, we see if the balance factory is 2 or -1. Anything between -1, 0, 1 are
   # okay. When imbalance is detected, if it's -2 (right heavy), we need to rotate left. But before
   # do that, we also see if the right child left heavy, if so, rotate it to the right first to make
   # the whole path truely right heavy. Then we can remote left. The opposite operation is done
   # when the it's left heavy
   def balance_tree(self):
      parent = self
      while parent:
         bfactor = parent.balance_factor()
         if bfactor == -2:
            if parent.right.balance_factor() == 1:
               parent.right.rotate_to_right()
            parent.rotate_to_left()
         elif bfactor == 2:
            if parent.left.balance_factor() == -1:
               parent.left.rotate_to_left()
            parent.rotate_to_right()
         parent = parent.parent
   
   # to rotate, here is the step:
   #     Pivot = Root.OS
   #     Root.OS = Pivot.RS
   #     Pivot.RS = Root
   #     Root = Pivot
   def rotate_to_right(self):
      # pivot is the left child of the root
      pivot = self.left

      # swap the pivot right child to the root's left child (which was the pivot)
      self.left = pivot.right
      if pivot.right: 
         pivot.right.parent = self

      # swap pivot and the root
      pivot.right = self
      self.parent, pivot.parent = pivot, self.parent

      # update the parent of the new root
      if pivot.parent:
         if pivot.parent.value < pivot.value:
            pivot.parent.right = pivot
         else:
            pivot.parent.left = pivot

   def rotate_to_left(self):
      # pivot is the right child of the root
      pivot = self.right

      # swap the pivot left child to the root's right child (which was the pivot)
      self.right = pivot.left
      if pivot.left: 
         pivot.left.parent = self

      # swap pivot and the root
      pivot.left = self
      self.parent, pivot.parent = pivot, self.parent

      # update the parent of the new root
      if pivot.parent:
         if pivot.parent.value < pivot.value:
            pivot.parent.right = pivot
         else:
            pivot.parent.left = pivot

   def height(self):
      if self.left or self.right:
         left_height = 0 if not self.left else self.left.height()
         right_height = 0 if not self.right else self.right.height()
         return 1 + max(left_height, right_height)
      else:
         return 0

   # balance factory of a node is the height of the left node (0 if not there) minus the height
   # of the right node (0 if not htere). The outcome value of -1, 0, 1 is considered balance. 
   # Anything greater or lesser than that, it's imbalance.
   def balance_factor(self):
      left_factor = 0 if not self.left else self.left.height()
      right_factor = 0 if not self.right else self.right.height()
      return left_factor - right_factor

sampletree = AVLTree(0)
for n in range(1,10):
   sampletree.root().insert(AVLTree(n))
sampletree = sampletree.root()
