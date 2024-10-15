'''
Author:Nandana Hasheed
Date:15-10-2024
Python program to determine the smallest of three numbers
'''
num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
num3=int(input("Enter num3"))
if(num1<num2 and num1<num3):
    print("num1",num1,"is the smallest")
elif(num2<num1 and num2<num3):
    print("num2",num2,"is the smallest")
else:
        print("num3",num3,"is the smallest")


