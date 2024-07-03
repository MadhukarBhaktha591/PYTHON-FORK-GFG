#08PythonProgramToConvertStringToList.py 

def Convert(string):
    li = list(string.split(" "))
    return li

str1 = "Geeks for Geeks"
print(Convert(str1))
print("\r")

def Convert(string):
    li = list(string.split("-"))
    return li

str1 = "Geeks-for-Geeks"
print(Convert(str1))
print("\r")

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

str1="ABCD"
print(Convert(str1))
print("\r")

import re 
def Convert(string):
    return re.findall('[a-zA-Z]',string)
str1="ABCD"
print("List of character is : ",Convert(str1))
print("\r")

s = "Geeks"
x = [i for i in s]
print(x)
print('\r')

s = "Geeks"
x = [i for a,i in enumerate(s)]
print(x)
print('\r')

import json
stringA = '["geeks",2,"for",4,"geeks",3]'
res = json.loads(stringA)
print("The converted list : \n",res)
print('\r')

import ast
ini_list = '["geeks",2,"for",4,"geeks",3]'
res = ast.literal_eval(ini_list)
print("The converted list : \n",res)
print(type(res))
print('\r')