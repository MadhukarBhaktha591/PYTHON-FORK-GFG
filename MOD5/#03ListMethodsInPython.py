#03ListMethodsInPython.py

List = ['Mathematics','Chemistry',1997,2000]
List.append(20544)
print(List)

#insert(pos,elem)

List.insert(2,2001)
print(List)

# List1.extend(List2)
List1 = [1,2,3,4,5,6,7,8]
List2 = [9,10,11,12,13,14,15,16]
List1.extend(List2)
print(List1)
print(List2)

# List1 += List2
# print(List1)

print(sum(List1))

# List1 = List1 - List2 ERROR: TYPE ERROR: UNSUPPORTED OPERAND
# print(List1)

List = ["HELLO",9]
# print(sum(List)) ERROR: TYPE ERROR: UNSUPPORTED OPERAND

print(List1.count(4))
print(len(List1))

element = List.pop()
print(element)
print(List)

print(*List)

del List2[0]
print(List2)
List2.remove(11)
print(List2)