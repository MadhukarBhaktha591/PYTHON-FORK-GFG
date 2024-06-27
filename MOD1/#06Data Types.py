#06Data Types.py
a = 5
print("Type of a ", type(a))

b = 5.0 
print("Type of b ", type(b))

c = 2 + 4j
print("Type of c ", type(c))

String1 = "Welcome to the Geeks world"
print("Type of String1 ", type(String1))
print(String1)

String1 = "I'm a geek"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1))

String1 = '''I'm a Geek and I live in a world of "Geeks" '''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))

String1 = '''Geeks
             For
             Life'''
print("\n Creating a multiline String: ")
print(String1)

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

print("\nFirst character of String is: ")
print(String1[0])

print("\nLast character of String is: ")
print(String1[-1])

List = []
print("Initial List: ", List)

List = ["Geeks", "For", "Geeks"]
print("List after adding three elements: ", List)
print(List[0])
print(List[2])
print(List[0] == List[2])

List = [['Geeks','For'],['Geeks']]
print("Multi-Dimensional List: ")
print(List)

List = ["Geeks", "For", "Geeks"]
print("Accessing elements using negative indexing")
print(List[-1])
print(List[-3])

Tuple1 = ()
print("Initial empty Tuple: ", Tuple1)

Tuple1 = ('Geeks','For')
print("Tuple after adding two elements: ", Tuple1)

list1 = [1,2,3,4,5,6]
print("\n Tuple using List: ")
print(tuple(list1))

Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

Tuple1 = (0,1,2,3)
Tuple2 = ('python','geek')
Tuple3 = (Tuple1,Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

tuple1 = tuple([1,2,3,4,5])
print("First element of tuple")
print(tuple1[0])

print("Last element of tuple")
print(tuple1[-1])

print("Third last element of tuple")
print(tuple1[-3])

print(type(True))
print(type(False))

# print(type(true)) 
# NameError

set1 = set()
print("Initial blank Set:", set1)

set1 = set("GeeksforGeeks")
print("Set with the use of function: ", set1)

set1 = set(["Geeks",'For','Geeks'])
print("Set with the use of list: ", set1)

set1 = set([1,2,'Geeks',4,'For',6,'Geeks'])
print("Set with the use of mixed values: ", set1)

set1 = set(["Geeks",'For','Geeks'])
print("Initial  Set:", set1)

print("Elements of set: ")
for i in set1:
    print(i, end =" ")

print("\n","Geeks" in set1)

Dict = {}
print("Initial blank Dictionary: ",Dict)

Dict = {1:'Geeks', 2:'For', 3:'Geeks'}
print("Dictionary with the use of Interger Keys: ", Dict)

Dict = {'Name':'Geeks', 1:[1,2,3,4]}
print("Dictionary with the use of Mixed Keys: ", Dict)

Dict = dict({1:'Geeks',2:'For',3:'Geeks'})
print("Dictionary with the use of dict(): ", Dict)
Dict = dict([(1,'Geeks'),(2,"For")])
print("\nDictionary with each item as a pair :",Dict)

Dict = {1:'Geeks', 'name':'For',3:'Geeks'}
print("Accessing a element using key:")
print(Dict['name'])

print("Accessing a element using get: ")
print(Dict.get(3))