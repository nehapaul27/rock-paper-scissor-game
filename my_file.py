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
---'    ____)____
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

game_images = [rock, paper, scissors]

user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid input, you lose!")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    else:
        if(computer_choice==user_choice):
            print("its a draw")
        elif (computer_choice==0 and user_choice==2):
            print("you loose")
        elif(user_choice==0 and computer_choice==2):
            print("you win")
        elif(computer_choice>user_choice):
            print("you loose")
        elif (user_choice>computer_choice):
            print("you win")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        