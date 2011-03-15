# Q: What is a graph? How to represent a graph? How to investigate a graph? What things can
# you do with it?

# A graph is a set of vertices and edges. Vertices are connected by edges. Graph can either
# directed and undirected graph. A graph can be represented by either adjacency-list or 
# adjacency-matrix. Adjancency-list is usually a preferred representation as it's compact. It's
# represented as a list (or in fact a map), each row/entry present a vertice. Each row/entry 
# points to a linked list of other vertices directly reachable from the verfice of the row. 
# Adjacency-matrix is represented as a matrix each row and column represent a verfice. The 
# intersection of row/column is set to value 1 (or other for other purpose) if the row node
# can reach the node column. The matrix requires more memory O(V^2). In undirected graph, matrix
# area under diagonal line sometimes can be dropped to save memory because the relationship
# can already be represented by the upper part.

# There are two ways to investigate a graph: breadth-first and depth-first. It makes use
# of color white, gray, and black to keep track of visiting state of nodes. It builds
# other data structures along the way. It has complexity of O(V+E) because we color all V
# nodes and it visits at most all edges in E.
#
# breadth-first(s, V, E):
#   for each v in V:
#      color[v] = 
#      distance[v] = infinity
#      parent[v] = nil
#   Q = { s }
#   distance[s] = 0
#   parent[s] = nil
#   while Q != { }:
#      u = q.dequeue()
#      for v in Adj[u] list in G
#         if v is white:
#            color[v] = gray
#            distance[v] = distance[u]+1
#            parent[v] = u
#            Q.enqueue(n)
#      color[u] = black
#
# The tree created by breadth-first search can be used to find out the shortest distance
# and path startin from the given root nodes.

# Depth-first search is antoher investigation. It has O(V+E) again because it go through
# nodes twice (2V) and visit only as many edges as in E. DFS creates DFS forest with sub
# trees. The time it tracks can be used for many application. The color can be used for
# detecting type of edges when a node is first visited: white = tree, gray = back, black =
# forward/cross. A cyclic graph can be dected by the presense of back edge. Need to know
# the start node????
#
# depth-first(V, E):
#   for each u in V:
#     color[u] = white
#     parent[u] = nil
#   time = 0
#   for each u in V:
#     if color[u] = white:
#       visit_node(u)
#
# visit_node(u):
#   color[u] = gray
#   start[u] = ++time
#   for each v in Adj[u]:
#     if color[v] = white:
#       parent[v] = u
#       visit_node(v)
#   color[u] = black
#   finish[u] = ++time
#
# One use of DFS is to do topilogical sort, which is the algorithm to find precedence of
# things given a directed acyclic graph. The way it works is simply running DFS on the the
# graph. As each node is finished, add it to the front of a linked list. The output list
# defines the order of things to preform.


