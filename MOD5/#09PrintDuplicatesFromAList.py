#09PrintDuplicatesFromAList.py

#BruteForceApproach
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1 
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

list1 = [10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
print(Repeat(list1))

#method2 using Counter() from collection module
from collections import Counter
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item]>1])
print(new_list)

#method3: Using count() method
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
new = []

for a in l1:
    n = l1.count(a)
    if n > 1:
        if new.count(a) == 0:
            new.append(a)
print(new)

#method4: using list comprehension method
def duplicate(input_list):
    return list(set([x for x in input_list if input_list.count(x) > 1]))
if __name__ == '__main__':
    input_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
    print(duplicate(input_list))

#method5: using list-dict approach
    # (without any inbuild count function)

def duplicate(input_list):
    new_dict, new_list = {}, []
    for i in input_list:
        if not i in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)
    return new_list
if __name__ == '__main__':
    input_list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
    print(duplicate(input_list))

#method6: in not in count()
lis = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)