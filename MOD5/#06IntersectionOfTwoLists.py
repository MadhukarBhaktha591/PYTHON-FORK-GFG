#06IntersectionOfTwoLists.py


#simplest no in-built functions used
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
lst1 = [15,9,10,56,23,78,5,4,9]
lst2 = [9,4,5,36,47,26,10,45,87]
print(intersection(lst1,lst2))

#use of set() method
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
lst1 = [15,9,10,56,23,78,5,4,9]
lst2 = [9,4,5,36,47,26,10,45,87]
print(intersection(lst1,lst2))

#set() the larger list, use built-in function intersection()
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))

#use of hybrid method  complexity FALLS TO O(n)
# Efficient way

def intersection(lst1,lst2):
    # use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3
lst1 = [9, 9, 74, 21, 45, 11, 63]
lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
print(intersection(lst1, lst2))

#meth 5 intersection is performed over sub-lists inside other lists.
# use the concept of filter() here

def intersection(lst1, lst2):
    lst3 = [list(filter(lambda x: x in lst1, sublist))for sublist in lst2]
    return lst3

lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection(lst1, lst2))