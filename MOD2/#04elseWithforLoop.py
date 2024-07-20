#04elseWithforLoop.py

for i in range(1,4):
    print(i)
else:
    print("No break")

def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("list contains an even number")
        else:
            print("list does not contain an even number")

print("For List 1:")
contains_even_number([1,9,8])
print("For List 2:")
contains_even_number([1,3,5])

count = 0
while (count < 1):
    count += 1
    print(count)
    break
else:
    print("No break")