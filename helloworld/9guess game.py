secret_num=9
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    num=int(input("Enter the num: Guess "))
    if num==secret_num:
        print("YOU WON")
        break
    else :
        print("try again")
        guess_count=guess_count+1
    if guess_count==guess_limit:
                 print("Sorry U have failed")
