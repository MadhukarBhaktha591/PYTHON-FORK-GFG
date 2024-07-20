#03YieldFunction.py

def print_even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i

test_list = [1,4,5,6,7]
print("The original list is : "+ str(test_list))

print("The even numbers in list are : ", end = " ")
for i in print_even(test_list):
    print(i, end = " ")
print("\r")

def nextSquare():
    i = 1
    while True:
        yield i*i
        i += 1

for num in nextSquare():
    if num > 100:
        break
    print(num)

def print_even(test_string):
    for i in test_string:
        if i == 'geeks':
            yield i

test_string = " There are many geeks around you, \
but only a few are geeks like you."

count = 0
print("The number of geeks is string is : ", end = "" )
test_string = test_string.split()

for i in print_even(test_string):
    count += 1

print(count)


