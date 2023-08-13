a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Enter the operator:")
x=input()
if x=='+':
    c=a+b
elif x=="-":
    c=a-b
elif x=="*":
    c=a*b
elif x=='/':
    c=a/b
elif x=='%':
    c=a%b
else:
    print("Enter a valid operator")
print("The output is:",c)