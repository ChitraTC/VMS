m1=int(input("Enter the first marks:"))
m2=int(input('Enter the second marks:'))
m3=int(input("Enter the third marks:"))

if(m1>m2):
    if(m2>m3) :
        total=m1+m2
    else:
        total=m1+m3
elif m1>m3 :
    total=m1+m2
else :
    total=m2+m3

avg=total/2
print("The averge of two best marks is  ",avg)