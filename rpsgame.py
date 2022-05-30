# importing the necessary packages
import random

# creating the instance of options

opt = ['rock', 'paper', 'scissors']

comp_guess = random.choice(opt)
user = input("State your choice: Rock, Paper, Scissors: ").lower()

if user not in opt:
    print('That seems out of option')
else:
    if user == comp_guess:
        print(f'You guessed {user} and the computer guessed {comp_guess} \n You won!!! Congratulations')
    else:
        print(f'You guessed {user} and the computer guessed {comp_guess} \n You did not win')