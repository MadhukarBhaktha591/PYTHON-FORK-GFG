#08PythonOperators.py
a = 9 
b = 4

add = a + b 
sub = a - b 
mul = a * b
div1 = a / b 
div2 = a // b
mod = a % b
p = a ** b

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(p)

x = 10000000000000000000006
if int(x / 2) == x // 2:
    print("Hello")
else:
    print("World")
 
a = 13
b = 33
print(a is b)
print(a is not b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

a = True
b = False
print(a and b)
print(a or b)
print(not a)

a = 10 
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

a = 10
b = a
print(b)

b += a
print(b)

b -= a
print(b)

b *= a 
print(b)

b <<= a
print(b)

a = 10 
b = 20 
c = a
print(a is not b)
print(a is c)

x = 24
y = 20
list = [10,20,30,40,50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

expr = 10 + 20 * 30
print(expr)

name = 'Alex'
age = 0 

if name == 'Alex' or name == 'John' and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye !!")

print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

print(5.0/2)
print(-5.0/2)
print(5//2)
print(-5//2)
print(5.0//2)
print(-5.0//2)

a , b = 10,20
min = a if a < b else b
print(min)

print((b, a) [a < b])

print({True: a, False: b} [a < b])

print((lambda: b, lambda: a)[a < b]())

print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")
a, b = 10, 20

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")

a = 5
b = 7
print(a,"is greater") if (a>b) else print(b,"is Greater")

a , b = 10, 20

min = a < b and a or b
print(min)