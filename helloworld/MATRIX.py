# initializing an empty matrix
matrix = []
# taking 2x2 matrix from the user
for i in range(2):
   # empty row
   row = []
   for j in range(2):
      # asking the user to input the number
      # converts the input to int as the default one is string
      element = int(input("ENTER THE ELEMENT: "))
      # appending the element to the 'row'
      row.append(element)
   # appending the 'row' to the 'matrix'
   matrix.append(row)
# printing the matrix
print(matrix)