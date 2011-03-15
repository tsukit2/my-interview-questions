# Q: What is minimum spanning tree? 

# A: Minimum spanning tree is a tree whose edges connect all the vertices in a graph where
# the total weight on all the edges is the mininum weight need to cover all the vertices. 

# Prim's minimum spanning tree can be used. The idea is simple. Start with a root node.
# Look at all reachable vertices and choose the one with minimum weight edge. Add that
# edge and the vertice. Now repeat the same process but to all vertices reachable from the
# the two vertices added already. Do this until no more vertices. All the edges
# represented the MST tree. Here is the algorithm
#
# MST-PRIM(r):
#   MST = { }
#   for v in V:
#      key[v] = infinity
#   key[r] = 0
#   Q = priority queue of all v in V-r based on key[v]
#   while Q != { }:
#      u = Q.minimum()
#      for each v in Adj[u]:
#         if v in Q and w(u,v) < key([v]:
#            MST.add(u,v)
#            key[v] = w(u,v)
#
# The algorithm takes roughly O(E log V) because the main loop executes only E times
# because vertices exhausted. Each loop takes log V from extracting the the minimum and
# adjusting the key weight in the last line.




