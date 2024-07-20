#05PythonStringMethodsSet1.py

string1 = "geeksforgeeks is for geeks"
string2 = "geeks"

print("The first occurrence of string2 is at : ", end="")
print(string1.find(string2,2))

print("The last occurrence of string2 ia at : ",end="")
print(string1.rfind(string2,8,20))
print("\r")

string1 = "geeks"
string2 = "geeksforgeeksportal"

if string2.startswith(string1):
    print("string2 begins with : "+string1)
else: print("string2 does not begin with : "+string1)

if string2.endswith(string1):
    print("string2 ends with : "+string1)
else: print("string2 does not end with : "+string1)
print("\r")

string1 = "GeeksforGeeks"
string2 = "geeks"

if string1.isupper() :
    print("string1 is in uppercase")
else:
    print("string1 is not in uppercase")

if string2.islower():
    print("string2 is in lowercase")
else:
    print("string2 is not in lowercase")
print("\r")

string1 = "GeeksForGeeks is fOr GeeKs"

str1 = string1.lower();
print("The lower case converted string is : " + str1)

str2 = string1.upper();
print("The upper case converted string is : " + str2)

str3 = string1.swapcase();
print("The swapped case converted string is : " + str3)

str4 = string1.title();
print("The title case converted string is : " + str4)
print("\r")