#04PythonModules.py

import calc 
from calc import add,subtract
from math import sqrt,factorial
from math import *
import sys
import math as madz
import random
import datetime
from datetime import date
import time

print(calc.add(10,2))
print(calc.subtract(44,22))

print(add(10,2))
print(subtract(44,22))

print(sqrt(16))
print(factorial(6))

print(sys.path)

print(madz.sqrt(69))

print(dir(madz))

print(madz.sqrt(25))
print(madz.pi)
print(madz.degrees(2))
print(madz.radians(60))
print(madz.sin(2))
print(madz.cos(0.5))
print(madz.tan(0.23))
print(madz.factorial(4))
print(random.randint(0,5))
print(random.random())
print(random.random()*100)

List = [1,4,True,800,"python",27,"hello"]
print(random.choice(List))

print(time.time())
print(date.fromtimestamp(454554))

