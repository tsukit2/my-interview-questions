
# bubble sort: keep repeatedly swapping items in each iteration until no swap is needed
# this has O(n^2) time and O(1) space because it's in-place sort. Good if the data sort of
# already sorted because only a couple swaps are needed
def bubble_sort(l):
   done = False
   max_size = len(l) - 1
   while not done:
      done = True
      for i in range(max_size):
         if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            done = False


# this is the improved version of bubble sort. This is done by counting the max index where
# the last swap happen. As the algorithm continues, the max index will come down. Keep track
# the highest index help skip many unnecessary swaps. This still has the same complexity
# it's just faster
def bubble_sort_optimized(l):
   n = len(l)
   while n > 1:
      newn = 0
      for i in range(n-1):
         if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            newn = i + 1
      n = newn

   
# insert sort: sort by partitioning the list between sorted and unsorted area beginng from the
# left side of the list. It starts with the first element assumed already inserted. Then it picks
# the next item and move along to each item in the sorted area to find the position of the item.
# As each next item is "inserted" into the sorted area, the boundary of the sorted area is 
# larger and larger until it occupies the entired list - thus the list is sorted. This has
# O(n^2) time and O(1) space. If the list is already sorted, it has O(n) as it doesn't have to
# to do anything. The worst case comes from a reversed list.
def insertion_sort(l):
   for par_index in range(len(l)-1):
      new_index = par_index + 1
      while new_index > 0 and l[new_index] < l[new_index-1]:
         l[new_index], l[new_index-1] = l[new_index-1], l[new_index]
         new_index -= 1


      
# selection sort: silimar to insertion sort exception the selected item in each iteration is
# the minimum value from the unsorted area, and it's swapped with the smallest number in the
# sorted are. Basically just pick the minimum at each iteration and line them up. It has O(n^2)
# time and O(1) space.
def selection_sort(l):
   max_size = len(l)
   for i in range(max_size-1):
      for j in range(i+1, max_size):
         if l[j] < l[i]:
            l[i], l[j] = l[j], l[i]



# merge sort: this is a divide-and-conquer approach. It doesn't sort in-place. It has O(n log n)
# time and O(n + log n) space and O(log n) for stack space. It's O(n log n) because it breaks down list into binary tree. The # of 
# levels of tree is log n. For each level, we go through pretty n element of that level. So
# roughly it's n log n. 
def merge_sort(l):
   def merge(left, right):
      result = []
      while left or right:
         if left and right:
            if left[0] <= right[0]:
               result.append(left[0])
               left = left[1:]
            else:
               result.append(right[0])
               right = right[1:]
         else:
            remain = left if left else right
            result.extend(remain)
            del remain[:]
      return result

   if len(l) <= 1: return l
   mid = round(len(l) / 2)
   left, right = l[:mid], l[mid:]
   left = merge_sort(left)
   right = merge_sort(right)
   return merge(left, right)


# quick_sort: this is another divide-and-conquer approach. It's different from merge sort that
# the partition is based on a pivot value. Pivot value can be selected in different ways:
# left-most, median value (in this implementation) or mediam of first/middle/last values. Since
# the partition is based on value, the merge is as simple as concatenating the partitions.
# This alogirhtm has O(n^2) and O(n log n) on average. The peroformance largely depends on the
# selection of the pivot value that could result to equal partition sizes. 
def quick_sort(l):
   if len(l) <= 1: return l
   left = []
   right = []
   pivot = []
   pivot_value = l[int(len(l) / 2)]
   for n in l:
      if n > pivot_value:
         right.append(n)
      elif n < pivot_value:
         left.append(n)
      else:
         pivot.append(n)
   return quick_sort(left) + pivot + quick_sort(right)


# quick sort inplace: this is similar to the original except that it sort elements in this
# to perform faster because there is no data copy. However, the complexity is still the same for
# time. Only space is improved.
def quick_sort_inplace(l, start, end):
   def partition(s, e, p):
      pval = l[p]
      l[p], l[e] = l[e], l[p]
      store = s
      for n in range(s, e):
         if l[n] <= pval:
            l[n], l[store] = l[store], l[n]
            store += 1
      l[store], l[e] = l[e], l[store]
      return store

   if start >= end: return
   pivot = partition(start, end, start + int((end-start) / 2))
   quick_sort_inplace(l, start, pivot-1)
   quick_sort_inplace(l, pivot+1, end)
   


