#09PatternMatchingInPythonWithRegex.py

#Python RegEx
import re
match = re.search(r'portal', 'GeeksforGeeks: A computer science \
                  portal for geeks')
print(match)
print(match.group())

print('Start Index:',match.start())
print('End Index:',match.end())
print('\r')

#Character Classes
print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: \
                 A computer science portal for geeks'))
print('\r')

#Ranges
print('Range',re.search(r'[a-zA-Z]','x'))
print('\r')

#Negation
print(re.search(r'[^a=z]','c'))
print('\r')

print(re.search(r'G[^e]','Geeks'))
print('\r')

import re
print('Geeks:',re.search(r'\bGeeks\b','Geeks'))
print('GeeksforGeeks',re.search(r'\bGeeks\b','GeeksForGeeks'))
print('\r')


#Beginning and End of String
match = re.search(r'^Geek','Campus Geek of the month')
print('Beg. of String:', match)

match = re.search(r'^Geek','Geek of the month')
print('Beg. of String:', match)

match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks')
print('End of String:', match)
print('\r')

#Any Character
print('Any Character',re.search(r'p.th.n','python 3'))
print('\r')

#Optional Characters
print('Color',re.search(r'colo?r','color'))
print('Colour',re.search(r'colou?r','colour'))
print('\r')

#Repetition
print('Date{mm-dd-yyyy}:',re.search(r'[\d]{2}-[\d]{2}-[\d]{4}','18-08-2020'))
print('Three digit:',re.search(r'[\d]{3,4}','189'))
print('Four digit:',re.search(r'[\d]{3,4}','2145'))
print('\r')

#Open-Ended Ranges
print(re.search(r'[\d]{1,}','5-th Floor, A-118,\
                Sector-136, Noida, Uttar Pradesh - 201305'))

#Shorthand
print(re.search(r'[\d]+','5th Floor, A-118,\
                Sector-136, Noida, Uttar Pradesh - 201305'))

# Grouping
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp)

#Return the entire match
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group())

#Return a tuple of matched groups
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.groups())

#Return a single group
grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020')
print(grp.group(3))

#Name your groups
match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})','26-08-2020')
print(match.group('mm'))

#individual match as a dictionary
match = re.search(r'(?P<dd>[\d]{2})-(?P<mm>[\d]{2})-(?P<yyyy>[\d]{4})','26-08-2020')
print(match.groupdict())

#Lookahead
print('negation:',re.search(r'n[^e]','Python'))
print('lookahead:',re.search(r'n(?!e)' ,'Python'))

#Positive Lookahead
print('positive lookahead',re.search(r'n(?=e)','jasmine'))

#Substitution
print(re.sub(r'([\d]{4})-([\d]{4})-([\d]{4})-([\d]{4})',r'\1\2\3\4','1111-2222-3333-4444'))

# compiled RegEx
regex = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})')
print('compiled reg expr',regex.search('26-08-2020'))
print(regex.sub(r'\1.\2.\3', '26-08-2020'))