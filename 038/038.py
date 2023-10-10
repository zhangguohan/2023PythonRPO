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

image = [rock, paper, scissors]
print("Let's play Rock Paper Scissors!")

while True:
    choice = input("Please choose (0 for Rock, 1 for Paper, 2 for Scissors): ")

    if not choice.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    choice = int(choice)

    if choice < 0 or choice > 2:
        print("Invalid choice! Please choose from 0, 1 or 2.")
        continue

    computer_choice = random.randint(0, 2)

    print(f"You chose {image[choice]}")
    print(f"Computer chose {image[computer_choice1]}")

    if choice == 0 and computer_choice == 2:

        print("Rock beats scissors, you win!")
    elif choice == 1 and computer_choice == 0:

        print("Paper beats rock, you win!")
    elif choice == 2 and computer_choice == 1:

        print("Scissors beats paper, you win!")
    elif choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lose!")

    play_again = input("Play again (y/n)? ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing!")
