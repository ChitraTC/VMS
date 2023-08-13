def countchar(word,letter):
    count=0
    for i in word:
        if i==letter :
            count=count+1
    return count

word=input("Enter a string:")
letter=input("Enter the character to be counted")
c=countchar(word,letter)
print("{0} appeared {1} times in {2}".format(letter,c,word))