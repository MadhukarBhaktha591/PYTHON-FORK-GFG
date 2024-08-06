#Code03.py

N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dishCount = 0
i = 0
while X >= 0 and Y >= 0 and dishCount != N:
    X -= A[i]
    Y -= B[i]
    if X >= 0 and Y >= 0:
        dishCount += 1
        i += 1
    print(X, Y, dishCount)
print(dishCount)
