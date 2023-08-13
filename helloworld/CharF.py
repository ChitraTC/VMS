word=input("Enter a string:")
for i in word:
    counter=0
    for letter in word:
        if letter == i:
            counter = counter+1

    print("The letter ",i,"occurred ",counter,"times",'in',word)