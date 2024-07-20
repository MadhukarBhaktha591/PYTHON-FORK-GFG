#03PrintEscapeCharactersinPython.py

ch = "I\nLove\tGeeksforgeeks"
print("The string after resolving escape character is :")
print(ch)

ch = "I\nLove\tGeeksforgeeks"
print("The string without repr() is:")
print(ch)

print("\r")

print("The string after using repr() is:")
print(repr(ch))

ch = "I\nLove\tGeeksforgeeks"
print("The string without r/R is:")
print(ch)

print("\r")
ch1 = r"I\nLove\tGeeksforgeeks"

print("The string after using r/R is:")
print(ch1)

print("\r")

ch2 = R"I\nLove\tGeeksforgeeks"

print("The string after using r/R is:")
print(ch2)