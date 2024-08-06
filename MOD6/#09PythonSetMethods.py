#09PythonSetMethods.py

#adding and removing elements

s = {'g','e','e','k','s'}

#adding 'f'
s.add('f')
print(s)  # Output: {'g', 'e', 'k', 's', 'f'}

s.discard('g')
print(s)  # Output: {'e', 'k', 's', 'f'}

s.remove('e')
print(s)  # Output: {'k', 's', 'f'}

print('\nPopped element',s.pop())
print('Set after updating:' , s)  # Output: {'s', 'f'}

s.clear()
print("Set after updating : ", s)  # Output: set()