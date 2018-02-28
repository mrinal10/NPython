'''
Created on 09-Feb-2018

@author: mailm
'''
from pip._vendor.distlib.compat import raw_input
from builtins import int


name = raw_input("Enter the name : ")
print("Hi ",name," How are you")
feeling = raw_input("How are you feeling today :")
print("It's good to know that you are",feeling)

print("Now it's time to check wheather a number is prime or not!!")
print("Please pick a number : ")
num = raw_input()

num = int(num)

# prime numbers are greater than 1
if num > 1:
   
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")