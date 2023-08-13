def CountChar(st,ch):
    count=0
    for i in st :
        if i==ch:
            count=count+1
    return count


st=input("Enter the string : ")
ch=input("enter the character to be counted : ")
c=CountChar(st,ch)
print("{0} appeared {1} times in {2}".format(ch,c,st))