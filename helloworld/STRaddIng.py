def add_string(str1):
  length = len(str1)

  if length <= 3:
      str1 += 'ing'
  else:
      str1 += 'ly'

  return str1
count=0
while count<=3:
    x=input("Enter the string :")
    print(add_string(x))
    count+=1