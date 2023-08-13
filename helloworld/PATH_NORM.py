# Python program to explain os.path.normpath() method

# importing os.path module
import os.path

# Path
path = '/home//user/Documnets'

# Normalize the specified path
# using os.path.normpath() method
norm_path = os.path.normpath(path)

# Print the normalized path
print(norm_path)

# Path
path = '/home/./Documents'

# Normalize the specified path
# using os.path.normpath() method
norm_path = os.path.normpath(path)

# Print the normalized path
print(norm_path)

# Path
path = '/home/user/temp/../Documents'

# Normalize the specified path
# using os.path.normpath() method
norm_path = os.path.normpath(path)

# Print the normalized path
print(norm_path)