#03range()Vsxrange().py
import sys
a = range(1,10000)
# x = xrange(1,10000)
print("The return type of range() is : ")
print(type(a))

# print("The return type of xrange() is :")
# print(type(x))

a = range(1,10000000)
# x = xrange(1,10000)
print("The size allotted using range() is :")
print(sys.getsizeof(a))
# print("The size allotted using xrange() is : ")
# print(sys.getsizeof(x))

a = range(1,6)
print("The list after slicing using range is : ")
print(a[2:5])
# print(a)