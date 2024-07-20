#05ControlStatementUsage

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print("Current Letter :{}".format(letter))

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print ('Current Letter :', letter)  #e appears first or s appears first

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

list = ['A','B','C','D']
l = len(list)
i = 1
while l-i >= 0:
    print(list[i-1])
    i += 1

for i in list:
    print(i)