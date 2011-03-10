# Q: Write function to walk tree in various function

# A: Walking tree has two major fashions: depth and breadth first. Depth-first walking has
# 3 different variation: post-, in-, and post-order

# sample tree
tree = ('f',
         (('b', 
           (('a', (None, None)),
            ('d',
              (('c', (None, None)),
               ('e', (None, None)))))),
          ('g',
           (None, 
            ('i', 
              (('h', (None, None)), 
               None))))))

         
# depth first pre order walk
def depth_first_pre_order_walk(t, result):
   result.append(t[0])                                      # node
   if t[1][0]: depth_first_pre_order_walk(t[1][0], result)  # left
   if t[1][1]: depth_first_pre_order_walk(t[1][1], result)  # right

# depth first in order walk
def depth_first_in_order_walk(t, result):
   if t[1][0]: depth_first_in_order_walk(t[1][0], result)  # left
   result.append(t[0])                                     # node
   if t[1][1]: depth_first_in_order_walk(t[1][1], result)  # right

# depth first post order walk
def depth_first_post_order_walk(t, result):
   if t[1][0]: depth_first_post_order_walk(t[1][0], result)  # left
   if t[1][1]: depth_first_post_order_walk(t[1][1], result)  # right
   result.append(t[0])                                       # node

# breadth first walk
def breadth_first_walk(t, result):
   q = [t]
   while q:
      t, q = q[0], q[1:]
      result.append(t[0])
      if t[1][0]: q.append(t[1][0])
      if t[1][1]: q.append(t[1][1])
   


