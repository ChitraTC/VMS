num=int(input("Enter the number:"))
if(num<=1):
    print(num," is not a prime number")
else:
    for i in range(2,num):
        print(i)
        if(num%i)==0:
            print(num," is not a prime number")
            break
    else:
        print(num," is a prime number")
