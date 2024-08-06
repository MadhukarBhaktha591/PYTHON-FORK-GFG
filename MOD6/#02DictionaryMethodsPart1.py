#02DictionaryMethodsPart1.py

dict1 = { 'Name':'Nandini', 'Age':19}

print("The constituents of dictionary as string are : ")
print(str(dict1))

print("The constituents of dictionary as list are : ")
print(dict1.items())

dict2 = { 'Name':'Nandini', 'Age':19, 'ID':239423}
li = [1,3,5,6]
print("The size of dic is : ",end="")
print(len(dict2))

print("The data type of dict2 is : ",end="")
print(type(dict2))

print("The type of li is : ",end="")
print(type(li))

dict3 = { 'Name':'Nandini', 'Age':19 }
dict4 = {}
dict4 = dict3.copy()
print('The new copied dictionary is : ')
print(dict4.items())

dict3.clear()
print('The new cleared dictionary is : ')
print(dict3.items())