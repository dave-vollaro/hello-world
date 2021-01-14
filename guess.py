#!/bin/csh
# guessing_game
# added test comment 7/10/20
import random
n=random.randint(1,99)
guess=int(input('Enter an integer from 1 to 99 '))
while n != guess:
    if guess < n:
        print('too low')
        guess=int(input('Enter an integer from 1 to 99 '))
    elif guess > n:
        print('too high')
        guess=int(input('Enter an integer from 1 to 99 '))
    else:
        print('you guessed it the number is ',guess)
        break
