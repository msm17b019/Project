'''
Author--Sujeet Kumar
Date--08/04/2021
Time--21:29

This code generates a random number and asks the user to guess it.
'''
import random # import random module to generate random number

num=random.randint(1,100) # random number will come in between 1 to 1000
count=0 #to know how many guesses were taken to guess the number

#run while loop to take input from user till user guess it correctly
while True:
    my_guess=int(input('Guess the number: '))
    if my_guess>num:
        print('Your guess is wrong. Lower number, Please!')
        count+=1
    elif my_guess<num:
        print('Your guess is wrong. Higher number, Please!')
        count+=1
    else:
        print('Your guess is right. It took you',count,'guesses.')
        break # break to come out of loop
        