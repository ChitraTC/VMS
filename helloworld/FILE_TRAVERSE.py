import os
def display_files():
# Set the directory to start from
    print("Enter path to traverse: ")
    root_dir = input()
    if os.path.exists(root_dir):
        dir_count = 0
        file_count = 0
    for dir_name, sub_dir_list, file_list in os.walk(root_dir):
        print(f"Found directory: {dir_name} \n")
# check to ignore starting directory while taking directory count
# normpath returns the normalized path eliminating double slashes etc.
        if os.path.normpath(root_dir) != os.path.normpath(dir_name):
            dir_count += 1
        for each_file_name in file_list:
            file_count += 1
            print(f"File name(s) {each_file_name} \n")
        print(f"Number of subdirectories are {dir_count} \n")
        print(f"Number of files are {file_count} \n")
        display_menu()
    else:
        print("Entered path doesn't exist")
        display_menu()
def display_menu():
    print("Enter your choice")
    print("Press 1 --> Display files and directories for a given path and their count")
    print("Press 2 --> Exit the program")
    choice = int(input())
    if choice == 1:
        display_files()
    else:
        exit()
if __name__ == "__main__":
    display_menu()