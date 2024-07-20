#05PythonClasses.py

#Classes are a way to group data and functions together
# class Dog:
#     pass

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def fun(self):
        print("Hello, my name is " + self.name )
        print("I am "+ str(self.age) + " years old")

Rodger = Dog("Rodger",5)
# Rodger.name = "Rodger"
# Rodger.age = 5

print(Rodger.name)
Rodger.fun()

# x = 0
# while (x < 100):
#     x += 2
# print(x)

class Person:
    def __init__(self,name) -> None:
        self.name = name
    def say_hi(self):
        print("Hello, my name is " + self.name)

p = Person('Madhukar')
p.say_hi()

class Dog:
    animal = 'dog'
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

Rodger = Dog("Pug","brown")
Buzo = Dog("Bulldog","black")

print('Rodger details:')
print('Rodger is a',Rodger.animal)
print('Breed:',Rodger.breed)
print('Color:',Rodger.color)

print('\nBuzo details:')
print('Buzo is a',Buzo.animal)
print('Breed:',Buzo.breed)
print('Color:',Buzo.color)

print("\nAccessing class variable using class name")
print(Dog.animal)

class Dog:
    animal = 'dog'
    def __init__(self, breed):
        self.breed = breed

    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())