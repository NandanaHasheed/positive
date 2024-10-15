'''
Author : Nandana Hasheed 
DAte: 15-10-2024
Python program to find the sum of digits 
num=int(input("Enter number"))
sum=0
while(num>0):
    r=num%10
    sum=sum+r
    num=num//10
print("Sum of digits",sum)
