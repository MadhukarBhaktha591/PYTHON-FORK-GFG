#09== EqualsISOperator
list1 = []
list2 = []
list3 = list1

if list1 == list2:
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

print(id(list1))
print(id(list2))
print(id(list3))

input1 = input()
print(input1)

num1 = int(input())
num2 = int(input())

print(num1 + num2)

num1 = float(input())
num2 = float(input())
print(num1 + num2)

string = str(input())
print(string)