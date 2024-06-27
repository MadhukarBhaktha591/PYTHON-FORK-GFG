#02Loops.py
#Loops are used to repeat a block of code multiple times
from __future__ import print_function
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("Loop ended")

n = 4
for i in range(0, n):
    print(i)

print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nString Iteration")
s = "geeksforgeeks"
for i in s:
    print(i)

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" %(i, d[i]))

print("\nSet Iteration")
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)

list = ["geeks","for","geeks"]
for index in range(len(list)):
    print(list[index])
    # if list[index] == "for": break    NOTE..IF BREAK..NO ELSE BLOCK
else:
    print("Loop ended")

# from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

fruits = ["apple","orange","kiwi"]
for fruit in fruits:
    print(fruit)

fruits = ["apple","orange","kiwi"]
iter_obj = iter(fruits)

while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break