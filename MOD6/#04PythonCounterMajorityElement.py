#04PythonCounterMajorityElement.py

from collections import Counter
def majorityElement(nums):
    freqDict = Counter(nums)
    size = len(nums)
    for key, value in freqDict.items():
        if value > size/2:
            print(key)
            return
    print('None')
if __name__ == "__main__":
    nums = [3,2,3]
    majorityElement(nums)