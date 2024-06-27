#10TypeConversion.py

x = 10
print("x is of type:",type(x))

y = 10.6
print("y is of type:",type(y))

z = x + y
print(z)
print("z is of type:",type(z))

s = "10010"
c = int(s , 2)
print("After converting to integer base 2 : ", end="")
print(c)

e = float(s)
print("After converting to float : ", end="")
print(e)

s = '4'
c = ord(s)
print("After converting character to integer : ", end="")
print(c)

c = hex(56)
print("After converting 56 to hexadecimal string : ", end="")
print(c)

c = oct(56)
print("After converting 56 to octal string : ", end="")
print(c)

s = 'geeks'
d = 'd'
c = tuple(s)
print("After converting string to tuple : ", end="")
print(c)
d = tuple(d)
print(d)
c += d
print(c) 

c = set(s)
print("After converting string to set : ", end="")
print(c)
d = set(d)
# c += d    error; unsupported for set +=
# print(c)


c = list(s)
print("After converting string to list : ", end="")
print(c)
c += "d"
print(c)

a = 1
b = 2
tup = (('a',1),('f',2),('g',3))
c = complex(1 ,2)
print("After converting integer to complex number : ",end="")
print(c)

c = str(a)
print("After convertig integer to string : ",end="")
print(c)

c = dict(tup)
print("After converting tuple to dictionary : ",end="")
print(c)

a = chr(76)
b = chr(77)

print(a)
print(b)

