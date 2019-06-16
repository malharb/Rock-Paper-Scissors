#rock paper scissors
#by malhar 16/06/19

import random
import time

choices = ['rock','paper','scissors']
messages = {"win":"Congratulations! You won","lose":"Hard luck! You lost","tie":"You tied!"}

user_choice = input("Please choose rock, paper or scissors: ")
user_choice = user_choice.lower()

computer_choice = choices[random.randint(0,2)]

print(f'You played {user_choice}')
print('The computer played...')
time.sleep(1)
print(f'{computer_choice}!')

if(user_choice == choices[0] and computer_choice == choices[2]):
    print(messages["win"])
elif(user_choice == choices[1] and computer_choice == choices[0]):
    print(messages["win"])
elif(user_choice == choices[2] and computer_choice == choices[1]):
    print(messages["win"])
elif(user_choice == choices[2] and computer_choice == choices[0]):
    print(messages["lose"])
elif(user_choice == choices[0] and computer_choice == choices[1]):
    print(messages["lose"])
elif(user_choice == choices[1] and computer_choice == choices[2]):
    print(messages["lose"])
else:
    print(messages["tie"])

input('Press ENTER to exit')
