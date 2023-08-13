# Python program to right rotate a list by n

# Returns the rotated list
def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list


# Driver Code
rotate_num = 5
list_1 = [4,5,6,7,8,9,10]

print(rightRotate(list_1, rotate_num))