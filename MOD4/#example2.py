#example2.py

def FizzBuzz(n):
    if n % 15 == 0: 
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
n = int(input("Enter the value for n : "))
print(FizzBuzz(n))
# 10 input neurons binary representation
# 1 hl = 25 neurons
# 4 output neurons