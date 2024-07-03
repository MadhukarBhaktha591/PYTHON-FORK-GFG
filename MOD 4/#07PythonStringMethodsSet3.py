#07PythonStringMethodsSet3.py 

String1 = "---geeksforgeeks---"
print("String after stripping all '-' is : ",end = "")
print(String1.strip('-'))

print("String after stripping all leading '-' is : ",end="")
print(String1.lstrip('-'))

print("String after stripping all trailing '-' is ",end="")
print(String1.rstrip('-'))
print("\r")

String1 = "geeksforgeeks"
print("The minimum value character is : " + min(String1))

print("The maximum value character is : " + max(String1))
print("\r")

# from string import maketrans # ERROR: ImportError
String1 = "geeksforgeeks"
String2 = "gfo"
String3 = "abc"

mapped = str.maketrans(String2,String3)
print("The string after translation using mapped elements is : ")
print(String1.translate(mapped))
print("\r")

String1 = "nerdsfornerds is for nerds"
String2 = "nerds"
String3 = "geeks"

print("The string after replacing strings is : ",end="")
print(String1.replace(String2, String3,2))
print("\r")

String1 = 'GEEKS\tFOR\tGEEKS'
print(String1)
print(String1.expandtabs())
print(String1.expandtabs(2))
print(String1.expandtabs(5))
print("\r")