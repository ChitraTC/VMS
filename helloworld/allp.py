s=input("Enter a string:")
for word in s.split(' '):
    if word==word[::-1]:
        print(word)