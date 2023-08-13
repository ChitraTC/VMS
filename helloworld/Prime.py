# Python program to check if the input number is prime or not
#Take input from the user
num = int(input("Please enter the number: "))
#Check if the given number is greater than 1
if num > 1:
   # Iterate through 2 to num/2.
   for i in range(2,num//2):
      #Select if the number is divisible by any number between 2 and num/2.
      if (num % i) == 0:
         print(num,"is not a prime number")
         print(i,"times",num//i,"is",num)
         break
      else:
         #If given number is not fully divisible by any number between 1 and num/2, then its prime.
         print(num,"is a prime number")
# Also, if the number is less than 1, its also not a prime number.
else:
   print(num,"is not a prime number")