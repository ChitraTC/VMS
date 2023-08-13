def add_string(str):
    length=len(str)

    if length <= 3:
        str+='ing'
    else:
        str+='ly'
    return str

count=0
while count<3:
    x=input("Enter a string :")
    print(add_string(x))
    count+=1