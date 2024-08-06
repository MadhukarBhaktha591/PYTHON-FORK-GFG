#01Dictionary.py
Dict1 = {1:'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict1)

#Creating a Dictionary
#with Integer Keys
Dict2 = {1:'Geeks', 2:'For', 3:'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict2)

#Creating a Dictionary
#with Mixed keys
Dict3 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict3)

#Creating an Empty Dictionary
Dict4 = {}
print("\nEmpty Dictionary: ")
print(Dict4)

#Creating a Dictionary 
#with dict() method
Dict5 = dict({1:'Geeks', 2:'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict5)

#Creating a Dictionary
#with each item as a Pair
Dict6 = dict([(1,'Geeks'), (2,'For'), (3,'Geeks')])
print("\nDictionary with each item as a pair: ")
print(Dict6)

#tc for crating a dictionary : O(len(dict))
#sc for creating a dictionary : O(n)

#NESTED DICTIONARY
Dict7 = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print("\nNested Dictionary: ")
print(Dict7)

#Adding elements to the dictionary
Dict8 = {}
print("Empty Dictionary: ")
print(Dict8)
Dict8[0] = 'Geeks'
Dict8[2] = 'For'
Dict8[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict8)

#Adding set of values to a single Key
Dict8['Value_set'] = 2,3,4
print("\nDictionary after adding 3 elements: ")
print(Dict8)

#Updating existing Key's Value
Dict8[2] = 'Welcome '
print("\nDictionary after updating value of an existing Key: ")
print(Dict8)

Dict8[2] = 'Welcome'
print("\n Updated key value: ")
print(Dict8)

#Adding Nested Key value to Dictionary
Dict8[4] = {'Nested' : {'1': 'Life', '2': 'Geeks'}}
print("\n Adding a Nested Key value: ")
print(Dict8)

Dict8[100] = "dummy add"
print("\n Adding a dummy key value: ")
print(Dict8)

Dict8[69] = "Random value less than prev key"
print("\n Adding a random key value: ")
print(Dict8)

#Accessing elements of a dictionary
Dict9 = {1:'Geeks','name':'For', 3:'Geeks'}

#accessing a element using key
print("\nAccessing a element using key: ")
print(Dict9['name'])

#accessing a element using key
print("\nAccessing a element using key: ")
print(Dict9[1])

#accessing a element using get() method
print("\nAccessing a element using get() method: ")
print(Dict9.get(3))

#Accessing an element of a nested dictinary
Dict10 = {'Dict1': {1:'Geeks'},
          'Dict2': {'name':'For'}}
print("\nAccessing an element of a nested dictinary: ")
print(Dict10['Dict1'])
print(Dict10['Dict1'][1])
print(Dict10['Dict2']['name'])

# Dictionary methods
# clear() - Remove all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# get() - Returns the value of specified key
# items() - Returns a list containing a tuple for each key value pair
# keys() - Returns a list containing dictionary's keys
# pop() - Remove the element with specified key
# popitem() - Removes the last inserted key-value pair
# update() - Updates dictionary with specified key-value pairs
# values() - Returns a list of all the values of dictionary

Dict11 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

#copy() method
Dict12 = Dict11.copy()
print(Dict12)

#clear() method
Dict11.clear()
print(Dict11)

#get() method
print(Dict12.get(1))

#items() method
print(Dict12.items())

#keys() method
print(Dict12.keys())

#pop() method
print(Dict12.pop(2))

#popitem() method
print(Dict12.popitem())

#update() method
Dict12.update({5: "C++", 6: "C"})
print(Dict12)

#values() method
print(Dict12.values())