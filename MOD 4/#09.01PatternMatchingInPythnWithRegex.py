#09.01PatternMatchingInPythnWithRegex.py

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print("\r")

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print("\r")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.groups())
print("\r")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
areaCode, mainNumber = mo.groups()
print(mainNumber)
print("\r")

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1))
print("\r")

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
print("\r")

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
print('\r')

haRegex = re.compile(r'(Ha){3}')
mo2 = haRegex.search('Ha')==None
print(mo2)
print('\r')

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
print('\r')

batRegex = re.compile(r'Bat(wo)?man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print('\r')

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
print('\r')

batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print('\r')

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo3.group())
print('\r')

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
print('\r')

batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo2.group())
print('\r')

batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batman') == None 
print(mo3)