#01PythonStrings.py

print("My name is Madhukar Bhaktha")

String1 = 'My name is Madhukar Bhaktha'
print("\nString with the use of Single Quotes")
print(String1)

String1 = "I'm a developer"
print("\nString with the use of Double Quotes")
print(String1)

String1 = '''I'm a developer and my nick name is "MadzTheDeveloper"'''
print("\nString with the use of Triple Quotes")
print(String1)

String1 = '''Multiple
lines
string'''
print("\nCreating a multiline String:")
print(String1)

String1 = 'GeeksForGeeks'
print("Initial String: ")
print(String1)

print("\nFirst Character of String is: ")
print(String1[0])

print("\nLast character of String is: ")
print(String1[-1])

gfg = "geeksforgeeks"
print(gfg[::-1])

gfg = "geeksforgeeks"
gfg = "".join(reversed(gfg))
print(gfg)

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

print("\nSlicing character from 3-12")
print(String1[3:12])

print("\nSlicing characters between" +
      "3rd and 2nd last character: ")
print(String1[3:-2])

String1 ="Hello, I'm a Geek"
print("Initial String")
print(String1)

list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("String after replacing 'e' with 'p'")
print(String2)

String3 = String1[0:2] + 'p' + String1[3:]
print(String3)

String1 = "Hello, I'm a Geek"
print("Initial String")
print(String1)

String1 = "Welcome to the Geek World"
print("Updated String: ")
print(String1)

String1 = "Hello, I'm a Geek"
print("Initial String")
print(String1)

String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)

String1 = "Hello, I'm a Geek"
print("Initial String")
print(String1)

del String1
print("\nDeleting the String: ")
# print(String1)  ERROR: NameError: name 'String1' is not defined

String1 = '''I'm a "Geek"'''
print("\nEscaping Single Quote: ")
print(String1)

String1 = "I'm a \"Geek\""
print("\nEscaping Double Quote: ")
print(String1)

String1 = 'I\'m a \"Geek\"'
print(String1)

String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backlashes: ")
print(String1)

String1 = "Hi\tGeeks"
print("\nTab: ")
print(String1)

String1 = "Python\nGeeks"
print("\nNew Line: ")
print(String1)

String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ")
print(String1)

String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ")
print(String1)

String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in Hexadecimal with the use of Escape Sequences: ")
print(String1)

String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)

String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print string in default order: ")
print(String1)

String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("Print string in specific order: ")
print(String1)

String1 = "{l} {f} {g}".format(g='Geeks',f='For',l='Life')
print("Print string in order of keywords: ")
print(String1)

String1 = "{0:b}".format(16)
print("Binary representation of 16 is ")
print(String1)

String1 = "{0:e}".format(165.6458)
print("\nExponential representation of 165.6458 is ")
print(String1)

String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)

String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks',
                                   'for',
                                   'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
                                                    2009)
print(String1)

Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' % Integer1)







