import random
rock='''
    _______
---'   ____)
       (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
          /______
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissor]

userChoice=int(input('What do you choose ? 0: Rock, 1: Paper, 2: Scissors= '))
AiChoice= random.randint(0,2)

print(f"User Choice={userChoice} , Ai Choice={AiChoice}")

if userChoice>2:
 print('sorry You lost because of an invalid number')
else:
 print(f"Your Choice:{images[userChoice]}")
 print(f"Ai Choice:{images[AiChoice]}")


if userChoice>2:
 print('Really Sorry')
elif userChoice==0 and AiChoice==2:
 print('You Won')

elif userChoice==2 and AiChoice==0:
 print('Ai Won')

elif AiChoice > userChoice:
 print('Ai Won')

elif AiChoice < userChoice:
 print('You Won')

elif AiChoice == userChoice:
 print('its a Draw')
