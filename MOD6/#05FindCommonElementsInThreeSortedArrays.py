#05FindCommonElementsInThreeSortedArrays.py
#By dictionary intersection

from collections import Counter
def commonElement(arr1,arr2,arr3):
    arr1=Counter(arr1)
    arr2=Counter(arr2)
    arr3=Counter(arr3)

    #perform intersection operation
    resultDict = dict(arr1.items() & arr2.items() & arr3.items())
    common = []

    for key,val in resultDict.items():
        for i in range(0,val):
            common.append(key)
    print(common)

if __name__ == "__main__":
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80,120]
    commonElement(arr1,arr2,arr3)