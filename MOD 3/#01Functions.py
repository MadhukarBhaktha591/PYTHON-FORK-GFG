#01Functions.py

def fun():
    print("My name is MADZ the developer")
fun()

def evenOdd(x):
    if x%2==0:
        print("Even")
    else:
        print("Odd")

evenOdd(2)
evenOdd(3)

def myFun(x, y= 50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

def student(firstName, lastName):
    print("First Name: ", firstName)
    print("Last Name: ", lastName)

student(firstName='Geeks',lastName='Practice')
student(lastName='Practice',firstName='Geeks')

def myFun(*argv):
    for arg in argv:
        print(arg, end=" ")
        print("\r")

myFun("hello", 'welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for',last = 'Geeks')

def evenOdd(x):
    """Function to check if the number is even or odd"""
    if x%2==0:
        print("Even")
    else:
        print("Odd")

print(evenOdd.__doc__)

def square_value(num):
    """Function to square the value of a number"""
    return num*num
print(square_value.__doc__)
print(square_value(2))
print(square_value(-4))

def myFun(x):
    x[0] = 20

lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)

def myFun(x):
    x = [20,30,40]

lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)

def myFun(x):
    x = 20
x = 10
myFun(x)
print(x)

def swap(x,y):
    x,y = y,x

x = 2
y = 3
swap(x,y)
print(x,y)

def cube(x) : return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

def f1():
    s = "geeksforgeeks"
    def f2():
        print(s)
    f2()
f1()
