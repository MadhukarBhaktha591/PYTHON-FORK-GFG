#06PythonStringMethodsSet2.py

string1 = "geeksforgeeks is for geeks"
print("The length of string is : ",len(string1))

print("Number of appearance of ""geeks"" is : ",end="")
print(string1.count("geeks",0,15))
print("\r")

string1 = "geeksforgeeks"
print("The string after centering with '-' is : ",end="")
print(string1.center(30,"-"))

print("The string after ljust is : ",end="")
print(string1.ljust(30,"-"))

print("The string after rjust is : ",end="")
print(string1.rjust(30,"-"))
print("\r")

string1 = "geeksforgeeks"
string2 = "123"

if string1.isalpha() :
    print("All characters are alphabets in string1")
else :
    print("Not all characters are alphabets in string1")

if string2.isalnum():
    print("All characters are alphanumeric in string2")
else:
    print("Not all characters are alphanumeric in string2")

if string1.isspace():
    print("All characters are spaces in string1")
else:
    print("Not all characters are spaces in string1")
print("\r")

string1 = "_"
string2 = ("geeks", "for", "geeks")
print("The string after joining is : ",end="")
print(string1.join(string2))
print("\r")