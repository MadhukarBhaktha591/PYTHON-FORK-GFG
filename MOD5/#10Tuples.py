#10Tuples.py

#Tuples are immutable
#Tuples are faster than lists
#Tuples are used to store heterogeneous data
#Tuples are used to store records
#Tuples are used to store coordinates
#Tuples are used to store points in time
#Tuples are used to store ranges
#Tuples are used to store keys in dictionaries
#Tuples are used to store values in dictionaries
#Tuples are used to store values in sets
#Tuples are used to store values in frozensets
#Tuples are used to store values in collections
#Tuples are used to store values in deque
#Tuples are used to store values in ordereddict
#Tuples are used to store values in defaultdict
#Tuples are used to store values in counter
#Tuples are used to store values in namedtuple
#Tuples are used to store values in chainmap
#Tuples are used to store values in deque

#Tuples created without the help of parenthesis are called Tuple Packing

Tuple1 = ()
print("Initial Empty Tuple: ")
print(Tuple1)

#Tuple with string
Tuple2 = ("Python", "is", "fun")
print("Tuple with string: ")
print(Tuple2)

#Tuple with the use of List
list1 = [1,2,3,4,5,6]
print("\nTuple using List: ")
print(tuple(list1))

#Create Tuple with built-in functions
Tuple3 = tuple("Python")
print("\nTuple using built-in functions: ")
print(Tuple3)

#Tuple with Mixed data type 
Tuple4 = (1, "Python", 3.0, "is", "fun")
print("\nTuple with Mixed data type: ")
print(Tuple4)

#Creating Tuple with nested Tuples
Tuple5 = (Tuple3,Tuple4)
print("\nTuple with nested Tuples: ")
print(Tuple5)

#Creating a Tuple with repetition
Tuple1 = ('Madz',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

#Create tuple with the use of Loops
Tuple1 = ('Geeks')
n = 5
for i in range(0, n):
    Tuple1 = (Tuple1,)
    print(Tuple1)

#accessing tuple with indexing
Tuple1 = ('Geeks', 'for', 'Geeks')
print("Accessing Tuple with Indexing: ")
print(Tuple1[0])

#Tuple unpacking
Tuple1 = ('Geeks', 'for', 'Geeks')
a,b,c = Tuple1
print("Tuple unpacking: ")
print(a)
print(b)
print(c)

#Concatenation of Tuples
Tuple1 = ('Geeks', 'for', 'Geeks')
Tuple2 = ('Geeks', 'for', 'Geeks')
Tuple3 = Tuple1 + Tuple2
print("Concatenation of Tuples: ")
print(Tuple3)

#Slicing of Tuples
Tuple1 = tuple('GeeksForGeeks')
print("Slicing of Tuples: ")
print(Tuple1[0:2])

#Reversing Tuple with slicing
# Tuple1 = ('Geeks', 'for', 'Geeks')
print("Reversing Tuple with slicing: ")
print(Tuple1[::-1])

print("\nPrinting elements between range 4-9: ")
print(Tuple1[4:9])

#Deleting a Tuple
#Tuples immutable..hence not allowe deletion

# entire tuple gets deleted by the use of del() method

#Deleting a Tuple
Tuple1 = (0,1,2,3,4)
try:
    del Tuple1
    print(Tuple1)
except NameError as n:
    print(n) #Output: name 'Tuple1' is not defined