## Code for Caesar Cipher technique starts
def encrypt_text(input_text, shift_pattern):
    cipher_result = ""
# Traverse the plain text
    for each_char in input_text:
# Check for empty spaces
        if each_char == " ":
            cipher_result = cipher_result + each_char
        elif each_char.isupper():
# Encrypt the uppercase characters in plain text
            cipher_result = cipher_result + chr((ord(each_char) + shift_pattern-65 ) % 26+65 )
        else:
# Encrypt the lowercase characters in plain text
            cipher_result = cipher_result + chr((ord(each_char) + shift_pattern - 97) % 26 + 97)

    return cipher_result

# # Code to apply Caesar Cipher technique end
def user_input():
    while True:
        print("Enter 1 to Encrypt the text using Caesar Cipher technique \n")
        print("Enter 2 to Exit the program \n")
        choice = int(input())

        if choice == 1:
            input_text = input("Enter a text: \n")
            shift_pattern = int(input("Enter Shift Pattern for encryption: \n"))
            encrypted_text = encrypt_text(input_text, shift_pattern)
            print(f"The encrypted text is {encrypted_text} \n")
        else :
            break
if __name__ == "__main__":
    user_input()