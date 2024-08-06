#08IntroductionToSets.py

#unordered
#iterable, mutable, no duplicate elements

#creating a set
set1 = set()
print("Initial blank Set: ")
print(set1)

#Creating a Set with the use of string
set1 = set("GeeksForGeeks")
print("Set with the use of string: ")
print(set1)

#Creating set with use of Constructor

String = 'GeeksForGeeks'
set1 = set(String)
print("Set with the use of an Object: ")
print(set1)

#Creating a set with the use of list
set1 = set(["Geeks","For","Geeks"])
print("Set with the use of list: ")
print(set1)

#Creating a set of list of Numbers(Having duplicate values)
set1 = set([10, 20, 30, 40, 20])
print("Set with the use of Numbers: ")
print(set1)

#Creating a Set with a mixed type of values
# having numbers and strings)

set1 = set([1,2,'Geeks',4,'For',6,'Geeks'])
print("Set with the use of mixed values: ")
print(set1)

#Adding elements to the set

#method1 using add() method

#Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

#Adding element and tuple to the set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("Set after adding elements: ")
print(set1)

#Adding elements to the Set using Iterator
for i in range(1,6):
    set1.add(i)
    
print("\nSet after Addition of elements from 1-5: ")
print(set1)

#Using Update() method
#for adding two or more elements

# to add elements to the set
# using update function
set1 = set([4,5,6,7])
set1.update([10,11])
print("\nSet after Addition of elements using Update: ")
print(set1)

#Accessing a Set

#creating a set
set1 =set(["Geeks","For","Geeks"])
print("\nInitial set")
print(set1)

#Access element using for loop
print("\nElements of set: ")
for i in set1:
    print(i)

print('Geeks' in set1)

#deletion of elements in a Set 
#using remove() method - KeyErroe if no elem found
#using discard() method - No keyerror

set1 = set([1,2,3,4,5,6
        ,7,8,9,10,11,12])
print("\nInitial set: ")
print(set1)

#method1 remove()
set1.remove(5)
set1.remove(6)

print("\nSet after removal of elements: ")
print(set1)

#method2 discard()
set1.discard(7)
set1.discard(8)
print("\nSet after Discarding two element: ")
print(set1)

#method3 using iterator method
for i in range(1,5):
    set1.remove(i)
print("\nSet after removal of elements: ")
print(set1)

#method4 using pop() method - to remove and RETURN
set1 = set([1,2,3,4,
            5,6,7,8,9,10,11,12])
print("Initial Set: ")
print(set1)

#Removing elemetn for the set..using pop() method
set1.pop()
print("\n Set after popping an element: ")
print(set1)

#using clear() method
set1 = set([1,2,3,4,5])
print("\nInitial set: ")
print(set1)

#removing all elements using clear() method
set1.clear()
print("\nSet after clearing all elements: ")
print(set1)

#FROZEN SETS 

String = ('G','e','e','k','s','F','o','r')
Fset1 = frozenset(String)
print("\nInitial frozenset: ")
print(Fset1)

#to print empty frozen set 
#no parameters passed
Fset2 = frozenset()
print("\nEmpty frozenset: ")
print(Fset2)

try:
    Fset1.add('M')
except AttributeError as ae:
    print(ae) #ERROR: 'frozenset' object has no attribute 'add'