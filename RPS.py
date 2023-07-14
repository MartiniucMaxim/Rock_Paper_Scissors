import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option_figures = [rock,paper,scissors]
option_names = ['Rock','Paper','Scissors']

player_input = int(input('What do you choose? Type 0 for rock, 1 for paper, 2 for Scissors.\nYour choice:'))
computer_input = random.randint(0,len(option_names)-1)

if player_input >= 0 and player_input <=2:
    print(f'Player choose:\n {option_figures[player_input]}')
    print(f'Computer choose:\n {option_figures[computer_input]}')
    
    if(player_input - computer_input)%3 == 1:
        print(f'Game over.{option_names[player_input]} beats {option_names[computer_input]}')
    elif(player_input == computer_input):
        print(f'Draw. \n{option_names[player_input]} equal {option_names[computer_input]}.\nYou both choose equal figures. Please try again.')
    else:
        print(f'Game over. {option_names[computer_input]} beats {option_names[player_input]}')
else: 
    print('You have entered number too low or too high for me')

        




