'''
Author - Sujeet Kumar
Date - 25/04/2021

This program Find power using recursion.
'''
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

num1=int(input())   #num1**num2 = num1 * num1 * num1 ........num2 times
num2=int(input())
print(power(num1,num2))