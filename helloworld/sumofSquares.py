import math
def sumofsquares(m):
    r=math.floor(math.sqrt(m))
    for j in range(1,r+1):
        for k in range(r,0,-1):
            if j**2+k**2==m:
                return True
    return False

x=int(input("Enter a number:"))
result=sumofsquares(x)
if result==True:
    print(x,"is a sum of square numbers")
else:
    print(x, "is not sum of square numbers")