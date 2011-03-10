# Q: Write function to compute fibonacci value. Fibonacci value of N, notated as F(n)
# equals to F(n-1) + F(n-2)

# A: This file provides 3 different implementation. The recusive implement is simplest but
# also the most naive and worst one. The dynamic programm, though has O(N) space, it can 
# be written to reused computed value. This means it can be reused over and over which is
# better than iterative. The iterative is the fast, good for a few computation.

# recursive implementation. This has O(2^n) time and space
def fibs_recursive(n):
   return n if n < 2 else fibs_recursive(n-1) + fibs_recursive(n-2)


# dynamic implementation. This has O(n) time and space.
def fibs_dynamic(n):
   if n < 2: return n
   mem = [0, 1]
   for i in range(2,n):
      mem.append(mem[i-1] + mem[i-2])
   return mem[n-1] + mem[n-2]


# iterative implementation. This has O(n) time and O(1) space
def fibs_iterative(n):
   if n < 2: fib = n
   else:
      fibn1, fibn2 = 1, 0
      i = 2
      while i != n:
         fibn1, fibn2 = fibn1+fibn2, fibn1
         i += 1
      fib = fibn1 + fibn2
   return fib   




