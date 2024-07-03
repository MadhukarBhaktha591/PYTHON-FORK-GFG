#example file.py
def xor(a,b):
    return (a|b)&(not(a&b))
def andof(a,b):
    return a&b 
def orof(a,b):
    return a|b
A, B = map(int,input("Enter A and B space separated either 1 or 0 : ").split())
print("XOR of A and B is : " + str(xor(A,B)))
print("AND of A and B is : " + str(andof(A,B)))
print("OR of A and B is : " + str(orof(A,B)))