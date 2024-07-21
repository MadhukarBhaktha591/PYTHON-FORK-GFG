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
Dict8[0] = 'Geeks'
Dict8[2] = 'For'
Dict8[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict8)



