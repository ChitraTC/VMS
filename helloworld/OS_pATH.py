# Python program to explain os.path.exists() method

# importing os module
import os

# Specify path
path = '/usr/local/bin/'
#path ='C:/Users/chitra/PycharmProjects/helloworld'


# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)