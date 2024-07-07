Var = ["Geeks","For","Geeks"]
print(Var)

#Creating a list in Python
List  = []
print("Blank List: ")
print(List)

List = [10,20,14]
print("List with Integer: ")
print(List)

List = ["Geeks","For","Geeks"]
print("List Items: ")
print(List[0])
print(List[2])
print("\r")

#Creating a List with multiple distinct or duplicate elements
List = [10,20,10,40,10,50,60,40]
print("List with the use of numbers:")
print(List)

List = [1,2,'Geeks',4,'For',6,'geeks']
print("List with the use of Mixed Values:")
print(List)
print("\r")

#accessing elements from the list
List = ['Geeks', 'For', 'Geeks']
print("Accessing elements from the list: ")
print(List[0])
print(List[2])
print("\r")

#accessing elements from the multi dimensional list
List = [['Geeks', 'For'],['Geeks']]
print("Accessing elements from the multidimensional list: ")
print(List[0][1])
print(List[1][0])
print("\r")

#negative indexing
List = [1,2,'Geeks',4,'For',6,'geeks']
print("Accessing elements using negative indexing")
print(List[-1])
print(List[-3])
print("\r")

#getting the size of python list
List1 = []
print(len(List1))

List2 = [10,20,14]
print(len(List2))
print("\r")

#taking input of a python list
string = input("Enter elements (Space-separated): ")
lst = string.split()
print('The list is: ',lst)

n = int(input("Enter the size of the list : "))
lst = list(map(int,input("Enter the integer \
elements of the list : ").strip().split()))[:n]
print("The list is : ",lst)
print("\r")

#adding elements to a python list
List = [1,2,3,4,5,6,7,8,9]
print("The list before adding elements:")
print(List)

List.append(10)
print("The list after adding elements:")
print(List)

#adding elements to the list using iterator
for i in range(1,4):
    List.append(i)
print("The list after adding elements:")
print(List)

#adding tuples to the list
List.append((12,13,14))
print("The list after adding tuples:")
print(List)

#adding list to the list
List.append([15,16,17])
print("The list after adding list:")
print(List)
print("\r")
# print(List[14][2])

#USING insert(pos,value) method
List = [1,2,3,4]
print("The list before inserting elements:")
print(List)

List.insert(3,12)
List.insert(0,'Geeks')
print("List after performing Insert Operation: ")
print(List)
print("\r")

#USING extend() method
List = [1,2,3,4]
print("The list before extending elements:")
print(List)

List.extend([8,'Geeks','Always'])
print("List after performing Extend Operation: ")
print(List)
print('\r')

#reversing a list
List = [1,2,3,4,5,6,7,8,9]
print("The list before reversing:")
print(List)
List.reverse()
print("The list after reversing:")
print(List)
print('\r')

#removing elements from the list
#USING remove() method

List = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Initial List: ")
print(List)

List.remove(5)
List.remove(6)
print("List after removing elements:")
print(List)
print('\r')

List = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(1,5):
    List.remove(i)
print("List after removing elements:")
print(List)
print('\r')

#Using pop() method
List = [1,2,3,4,5]
print("Initial List: ", List)
List.pop()
print("List after popping an element: ")
print(List)

List.pop(2) #index 2
print("List after popping an specific element: ")
print(List)
print("\r")

#Slcing of a List
List = ['G','e','e','k','s','f','o','r','G','e','e','k','s']
print("Initial List: ", List)
print(List[:6])
print(List[:-4])
print(List[4:])
print(List[4:8])
print(List[::-1])
print(List[:])
print(List[-6:-1])

#List comprehension
odd_square = [x ** 2 for x in range(1,11) if x % 2 == 1]
print(odd_square)

odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print(odd_square)

#copying a list and deleting it... .copy() .clear()
new_list = odd_square.copy()
print(new_list)
new_list.clear()
print(new_list)