# Q: What is B-Tree? What is it good at for? Describe its opertions.

# A: B-Tree is like other self-balancing tree such as AVL and red-black tree such that it maintains
# its balance of nodes while opertions are permormed against it. B-Tree has the following properties:
#     - minimum degree "t" where, except root node, all other nodes must have no less than t-1 keys
#     - each node with n keys has n+1 children
#     - keys in each node are lined up where k1 < k2 < .. Kn
#     - Each node cannot have more than t2-1 keys, thus 2t children
#     - Root node at least must contains one key. There is no root node is the tree is empty
#     - tree grows in depth only when root node is split
# 
# To search the tree, it's as bother binary tree except that the key is compared multiple times
# in a given node because node contains more than 1 keys. If the key is found in the node, the
# search terminates. Otherwise, it moves down where at child pointed by ci where key k < ki.
#
# Key insertions of a B-tree happens from the bottom fasion. This means that it walk down the
# tree from root to the target child node first. If the child is not full, the key is simply 
# inserted. If it is however, the child node is split in the middle, the median key moves up to
# the parent, then the new key is inserted. When inserting and walking down the tree, if the
# root node is found to be full, it's split first and we have new root node. Then the normal
# insertion operation is performed.
#
# Key deletion is more complicated as it needs to maintains the # of keys in each node to meet
# the constraint. If key is found in leaf node and deleting it still keep # of keys in the nodes
# not too low, it's simply done right away. If it's done to the inner node, the predecessor of
# of the key in the corresonding child node is moved to replace the key in the inner node. If
# moving the predecessor will cause the child node to violate the node count constraint, the 
# sibling child nodes are combined and the key in the inner node is deleted. (More to this but
# it's very complicated)

