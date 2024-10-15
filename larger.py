'''
Author:Nandana Hasheed
Date:15-10-2024
Python program to determine the largest of two numbers
'''
num1=int(input("Enter num1:"))
num2=int(input("Enter num 2:"))
if(num1>num2):
    print("num 1:",num1,"is greater than num 2:",num2)
elif(num2>num1):
    print("num 2 :",num2,"is greater than num 1:",num1)
else:
    print("Both numbers:",num1,"&",num2,"are equal")
