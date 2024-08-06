#07SwitchCaseInPython.py 

#method1 using dictionary mapping
def numbers_to_string(argument):
    switcher = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
    }
    return switcher.get(argument, "Invalid Number")

if __name__ == "__main__":
    argument = 0
    print(numbers_to_string(argument))

#Method2 if-else

fruit = "Yamaha"

if fruit == "Hero":
    print("letter is Hero")
elif fruit == "Suzuki":
    print("letter is Suzuki")
elif fruit == "Yamaha":
    print("fruit is Yamaha")
else:
    print("Please choose correct answer")

#method3 : switch case using Class
    
class Python_Switch:
    def day(self, month):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(month), lambda: default)()
    def case_1(self):
        return "Jan"
    def case_2(self):
        return "Feb"
    def case_3(self):
        return "Mar"
    
my_switch = Python_Switch()

print(my_switch.day(1))

print(my_switch.day(3))

#using match

def numbers_to_string(argument):
    match argument:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case default:
            return "Invalid Number"
        
if __name__ == "__main__":
    argument = 0
    print(numbers_to_string(argument))