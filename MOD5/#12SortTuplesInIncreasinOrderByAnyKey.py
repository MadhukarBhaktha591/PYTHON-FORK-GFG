# #12SortTuplesInIncreasinOrderByAnyKey.py
# Input : tuple = [(2, 5), (1, 2), (4, 4), (2, 3)] 
#             m = 0
# Output : [(1, 2), (2, 3), (2, 5), (4, 4)]
# Explanation: Sorted using the 0th index key.

# Input :  [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
#          m = 2
# Output : Sorted: [(23, 45, 20), (89, 40, 23), (25, 44, 39)] 
# Explanation: Sorted using the 2nd index key

#get the last key
def last(n):
    return n[m]

#function to sort the tuple
def sort(tuples):
    return sorted(tuples, key=last)

a = [(23,45,20),(25,44,39),(89,40,23)]
m = 2
print("Sorted: ",sort(a))