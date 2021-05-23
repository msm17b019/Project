'''
Author--Sujeet Kumar
Date--08/04/2021
Time--17:47

This code is for snake, water and gun game.
'''
import random  #random module is needed to play this game with computer

#create a list and put all options in it
options=['snake','water','gun']

#Let computer randomly choose its option
comp=random.choices(options)
comp=str(comp)
comp=comp.replace('[\'','')
comp=comp.replace('\']','')

#now you choose your option
print('Choose one option --','\n snake \n water \n gun')
your_option=input('Enter your option : ')
your_option=your_option.lower()

#Now decide who wins or it is draw
if your_option=='snake' and comp=='water':
    print('You Win')
elif your_option=='water' and comp=='gun':
    print('You Win')
elif your_option=='gun' and comp=='snake':
    print('You Win')
elif comp=='snake' and your_option=='water':
    print('You Lose')
elif comp=='water' and your_option=='gun':
    print('You Lose')
elif comp=='gun' and your_option=='snake':
    print('You Lose')
elif your_option==comp:
    print('Game Draw')
else:
    print('Invalid option. Please enter option as per above.')
