#07LambdaFunction.py
string = 'GeeksForGeeks'
print(lambda string : string)

x = 'GeeksforGeeks'
(lambda x:print(x))(x)

def cube(y):
    return y*y*y

lambda_cube = lambda y:y*y*y

print(cube(5))
print(lambda_cube(5))

tables = [lambda x=x:x*10 for x in range(1,11)]
for table in tables:
    print(table())

Max = lambda a,b : a if(a>b) else b
print(Max(1,2))

List = [[2,3,4],[1,4,16,64],[3,6,9,12]]

sortList = lambda x : (sorted(i) for i in x)
secondLargest = lambda x,f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List,sortList)
print(res)

li = [5,7,22,97,54,62,77,23,73,61]

final_list = list(filter(lambda x:(x%2 != 0),li))
print(final_list)

ages = [13,90,17,59,21,60,5]
adults = list(filter(lambda age: age>18, ages))
print(adults)

li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(map(lambda x:x*2,li))
print(final_list)

animals = ['dog','cat','parrot','rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)

from functools import reduce
li = [5,8,10,20,50,100]
sum = reduce((lambda x,y:x+y),li)
print(sum)

import functools
lis = [1,3,5,6,2]
print("The maximum element of the list is : ",end="")
print(functools.reduce(lambda x, y: x if x > y else y, lis))
