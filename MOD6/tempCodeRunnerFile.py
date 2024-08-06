set1 = set([4,5,6,7])
set1.update([10,11])
print("\nSet after Addition of elements using Update: ")
print(set1)

#Accessing a Set

#creating a set
set1 =set(["Geeks","For","Geeks"])
print("\nInitial set")
print(set1)

#Access element using for loop
print("\nElements of set: ")
for i in set1:
    print(i)

print('Geeks' in set1)