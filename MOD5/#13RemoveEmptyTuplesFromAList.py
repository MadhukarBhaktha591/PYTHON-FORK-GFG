# #13RemoveEmptyTuplesFromAList.py

# Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                   ('krishna', 'akbar', '45'), ('',''),()]
# Output : [('ram', '15', '8'), ('laxman', 'sita'), 
#           ('krishna', 'akbar', '45'), ('', '')]

# Input : tuples = [('','','8'), (), ('0', '00', '000'), 
#                  ('birbal', '', '45'), (''), (),  ('',''),()]
# Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '', 
#           '45'), ('', '')]

#method1: use list comprehension
def Remove(tuples):
    return [t for t in tuples if t != () and t != ('', '')]
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

#method2: Using filter() method
def Remove(tuples):
    return list(filter(lambda x: x != () and x != ('', ''), tuples))

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

#method3: Using len() method
def Remove(tuples):
    return [t for t in tuples if len(t) > 0]
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

#method4: Using == operator. check if tuple == empty tuple () and remove if equals
def Remove(tuples):
    for i in tuples:
        if i == ():
            tuples.remove(i)
    return tuples
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))