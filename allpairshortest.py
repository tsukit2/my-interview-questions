# Q: How to compute all-pair shortest path. How to construct the path?

# A: We can use Floyd-Warshal algorithm. The idea is based on the observation that, a path between
# vertice i and j composes of vertices i..k,j. Recursively, the vertices from i..k
# compoese of i..k-1,k so on and so forth until i and k are immediately connected. His
# algorithm uses matrix of nxn where n is the number of vertices and calculate from the
# bottom up as following.
#
# Note that there are two matrices constructed at the same time. One is the shortest
# path value and the other is predecessor matrix.
#
# Floyd-Warshal(W):
#   n = rows[W]
#   M = W  <-- matrix initialized with weight of immediately connected node. Any
#              non-existing slots are set to infinity.
#   P = ...<-- matrix initialized with predecessor immediately accessible. Predecessor of
#              itself or non-existing immediate access is set to NIL.
#   for k = 1 to n:
#      for i = 1 to n:
#          for j = 1 to n:
#              M[i,j] = min(M[i,j], M[i,k] + M[k,j])
#              P[i,j] = M[i,j] if M[i,j] <= M[i,k] + M[k,j]
#                       M[k,j] otherwise
#
# This algorith takes O(V^3) as it has 3 inner loops.
#
# To construct a path, just walk the matrix backward starting i,j then i,k -> i,k-1...

# With this shortest information in place, a simple version of travelling sales problem can be
# very easily. Given vertices A, B, C, D to travel. Just pick the shortest path between
# (A,B), (A,C), and (A,D). Say C is chosen, further find shortest path between (C,B) and
# (C,D). When done that's the first answer. The path (A,C,B,D) can then be swap between
# two vertices and calculate the path. This iteration can be as long as need to see if
# the shorter path can be obtained.
