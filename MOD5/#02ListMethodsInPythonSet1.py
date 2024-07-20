#02ListMethodsInPythonSet1.py 

lis = ["geekst","for","geeks"]
#len(lis)
print("Length of the list is : ",end="")
print(len(lis))

#min(lis)
print("The minimum element of list is : ",end="")
print(min(lis))

#max(lis)
print("The maximum element of list is : ",end="")
print(max(lis))

# lis.sort()
# print(lis)

#index(ele,beg,end)
List = [1,2,3,1,2,1,2,3,2,1]
print(List.index(2))
print(List.index(2,2,9))

#count()
print(List.count(2))