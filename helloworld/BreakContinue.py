sum=0
count=0
while True:
    x=int(input("Enter a number:"))
    if x%2 !=0:
        continue
    else:
        sum+=x
        count+=1
    if count==5:
        break
print("Sum= ", sum)