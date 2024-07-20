#05UnionOfTwoOrMoreLists.py

#Maintaining Repetition
def Union(lst1,lst2):
    final_list = lst1 + lst2
    return final_list
lst1 = [23,15,2,14,14,16,20,52]
lst2 = [2,48,15,12,26,32,47,54]
print(Union(lst1,lst2))

#Maintaining both repetiotion and order
def Union(lst1,lst2):
    final_list = sorted(lst1 + lst2)
    return final_list
lst1 = [23,15,2,14,14,16,20,52]
lst2 = [2,48,15,12,26,32,47,54]
print(Union(lst1,lst2))

#Without repetition
def Union(lst1,lst2):
    final_list = list(set(lst1 + lst2))
    return final_list
lst1 = [23,15,2,14,14,16,20,52]
lst2 = [2,48,15,12,26,32,47,54]
print(Union(lst1,lst2))

#Union of more than 2 lists
def Union(lst1,lst2,lst3):
    final_list = list(set().union(lst1, lst2, lst3))
    return final_list
lst1 = [23,15,2,14,14,16,20,52]
lst2 = [2,48,15,12,26,32,47,54]
lst3 = [4,78,5,6,9,25,64,32,59]
print(Union(lst1,lst2,lst3))

#using extend method
lst1 = [23,15,2,14,14,16,20,52]
lst2 = [2,48,15,12,26,32,47,54]
lst1.extend(lst2)
print("Maintaining Repetition "+str(lst1))
x = list(set(lst1))
print("Without Repetition "+str(x))