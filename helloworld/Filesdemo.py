f=open("romeo.txt","w")
count=0
for line in f:
    count+=1
    print("line number",count,":",line.rstrip())
print("Total lines=",count)
f.close()
