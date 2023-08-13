import re
# Function to Find all the patterns of "1(0+)1" in a given string
def check_uc_lc_pattern(user_input):
    # regex
    pattern = re.compile("[A-Z]+[a-z]+$")
    # searching pattern
    if pattern.search(user_input):
        print("String pattern match success \n")
    else:
        print("String fails the pattern \n")

def menu():
    while True:
        print("1 --> Identify a word with a sequence of one upper case letter followed by lower case letters")
        print("2 --> Exit the program")
        choice = int(input("Enter a number to perform any of the operation: "))
        print("\n")
        if choice == 1:
            user_input = input("Enter a string with a sequence of Upper and Lower case letters: ")
            print("\n")
            check_uc_lc_pattern(user_input)
        else:break
# Main
if __name__ == "__main__":
    menu()