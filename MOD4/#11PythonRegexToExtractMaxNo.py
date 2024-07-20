#11PythonRegexToExtractMaxNo.py 

import re
# Also works code by vs code 
# def extractMaxNo(string):
#     pattern = r'\d+'
#     result = re.findall(pattern, string)
#     return max(result)
# if __name__=="__main__":
#     string = "The number is 1234567890"
#     print(extractMaxNo(string))

def extractMax(input):
    numbers = re.findall('\d+',input)
    numbers = map(int,numbers)
    print(max(numbers))

if __name__ == "__main__":
    input = '100lh564abc365bg'
    extractMax(input)