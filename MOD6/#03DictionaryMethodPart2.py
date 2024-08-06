#03DictionaryMethodPart2.py

dict1 = {'Name':'Nandini' , 'Age':19 }
dict2 = {'ID':353928}
sequ = ('Name','Age','ID')
dict1.update(dict2)
print("The updated dictionary is : ")
print(str(dict1))

# using fromkeys() to transform sequence into dictionary
dict3 = dict.fromkeys(sequ,3)
print("The new dictionary values are : ")
print(str(dict3))

dict = {'Name' : 'Nandini', 'Age' : 19}

# if dict.has_key('Name'): has_key() method removed in Python 3
if 'Name' in dict:
    print("Name is a key")
else:
    print("Name is not a key")

print("The value associated with ID is : ")
print(dict.get('ID', "Not Present (default printed)"))

#printing dictionary values
print("The dictionary values are : ")
print(str(dict))

print("The value associated with Age is : ",end="")
print(dict.setdefault('ID', "no ID"))

#printing dictionary values
print("The dictionary values are : ")
print(str(dict))