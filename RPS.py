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

#Write your code below this line 👇
option = [rock,paper,scissors]
player_input = input('What do you choose? Type 0 for rock, 1 for paper, 2 for Scissors')
player_choice = int(player_input)
computer_input = int(random.randint(0,len(option)-1))

player_option = option[int(player_input)]
computer_option = option[int(computer_input)]

# if (player_option == option[1] and )
if(player_option == option[1] and computer_option == option[0]):
    print(f"{option[1]}")
    print(f"{option[0]}")
    print('Game over. Paper beats rock')
elif(player_option == option[1] and computer_option == option[2]):
    print(f"{option[1]}")
    print(f"{option[2]}")
    print('Game over. Scissors beats paper')
elif(player_option == option[0] and computer_option == option[1]):
    print(f"{option[0]}")
    print(f"{option[1]}")
    print('Game over. Paper beats rock')
elif(player_option == option[0] and computer_option == option[2]):
    print(f"{option[0]}")
    print(f"{option[2]}")
    print('Game over. Rock beats scissors')
elif(player_option == option[2] and computer_option == option[0]):
    print(f"{option[2]}")
    print(f"{option[0]}")
    print('Game over. Rock beats scissors')
elif(player_option == option[2] and computer_option == option[1]):
    print(f"{option[2]}")
    print(f"{option[1]}")
    print('Game over. Scissors beats paper')
elif(player_option == computer_option):
    print(f"{player_option}")
    print(f"{computer_option}")
    print('Draw. Try again')
else:
    print('You\'re out ob boundary')


        



# option_rock = option[0]
# option_paper = option[1]
# option_scissors = option[2]



