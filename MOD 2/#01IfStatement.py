#01IfStatement.py
i  = 10

if (i > 15):
    print("10 is less than 15")
print("I am not in if")

i = 20
if (i < 15):
    print("i is less than 15")
    print("i'm in if Block")
else:
    print("i is not less than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")

def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum = dsum + int(ele)
    return dsum

List = [367, 111, 562, 945, 6736, 873]
newList = [digitSum(i) for i in List if i & 1]
print(newList)

i = 10
if (i == 10):
    if (i < 15):
        print("i is less than 15")
    if (i < 12):
        print("i is less than 12 too")
    else:
        print("i is greater than 15")

i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")

i = 10
if i < 15:print("i is less than 15")

i = 10
print(True) if i < 15 else print(False)
