#07NumbersInAListWithinAGivenRange.py
#Given a list of numbers and a range, return the numbers in the list that fall within the range
def count(list1,l,r):
    c = 0
    for i in list1:
        if i >= l and i <= r:
            c += 1
    return c
list1 = [10,20,30,40,50,40,40,60,70]
l = 40
r = 80
print(count(list1, l, r))

#single line approach
def count(list1,l,r):
    return len(list(x for x in list1 if l <= x <= r))
list1 = [10,20,30,40,50,40,40,60,70]
l = 40
r = 80
print(count(list1, l, r))

#using sum() 
def count(list1,l,r):
    return sum(1 for x in list1 if l <= x <= r)
list1 = [10,20,30,40,50,40,40,60,70]
l = 40
r = 80
print(count(list1, l, r))