#04SortListAccordingToLengthOfElemnts.py

list1 = ["rohan", "amy", "sapna",
          "muhammad",
                "aakash", "raunak", "chinmoy"]
list2 = [["ram", "mohan", "aman"], ["gaurav"], 
                 ["amy", "sima", "ankita", "rinku"]]

#create new list: sorted()
sorted_list = sorted(list1, key=len)
print(list1)
print(sorted_list)

list1.sort(key=len)
print(list1)

#code for sorting creating a new dummy list
import numpy
def Sorting(lst):
      lenlist = []
      for i in lst:
            lenlist.append(len(i))
      
      sortedIndex = numpy.argsort(lenlist)
      lst2 = ['dummy'] * len(lst)

      for i in range(len(lst)):
            lst2[i] = lst[sortedIndex[i]]
      return lst2


list1 = ["rohan", "amy", "sapna",
          "muhammad",
                "aakash", "raunak", "chinmoy"]
print(Sorting(list1))
print("\r")