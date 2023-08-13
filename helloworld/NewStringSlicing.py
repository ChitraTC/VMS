def string_slicing_both_ends(str):
    if len(str)<2:
        return''
    return str[0:2]+str[-2:]

s=input("Enter a string :")
r=string_slicing_both_ends(s)
print("The new string",r)