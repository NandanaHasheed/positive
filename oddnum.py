'''
Author:Nandana Hasheed
Date:15-10-2024
Python program to generate odd numbers upto n
'''
limit=int(input("Enter the limit"))
odd_number=1
while odd_number<=limit:
    print(odd_number,"\t",end="")
    odd_number+=2