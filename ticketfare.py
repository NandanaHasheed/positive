'''
Author:Nandana Hasheed
Date:15-10-2024
Python program to determine the entry ticket fare in a zoo
'''
age=int(input("Enter age"))
if(age<10):
    print("Fare = 7")
elif(age>=10 and age<60):
     print("Fare = 10")
else:
     print("Fare =5")
