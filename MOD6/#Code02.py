#Code02

H,W = map(int,input().split())
Si, Sj = map(int,input().split())
H -= 1
W -= 1
Si -= 1
Sj -= 1
C=[]
for i in range(H+1):
  row = list(map(str,input().split()))
  C.append(row)
X = str(input())


for x in X:
  if Si!= 0 and x == "U":
    if C[Si-1][Sj] == ".":
      Si -= 1
    #   print("up")
  if Si != H and x == "D":
    if C[Si+1][Sj] == ".":
      Si += 1
    #   print("down")
  if Sj != 0 and x == "L":
    if C[Si][Sj-1] == ".":
      Sj -= 1
    #   print("left")
  if Sj != W and x == "R":
    if C[Si][Sj+1] == ".":
      Sj += 1
    #   print("right")
print(Si+1, Sj+1)