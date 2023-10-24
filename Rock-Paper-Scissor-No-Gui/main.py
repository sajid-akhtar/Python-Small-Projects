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


def resultA(user, computer) -> bool:
    if user == 0 and computer == 1:
        return False
    elif user == 1 and computer == 2:
        return False
    elif user == 2 and computer == 0:
        return False
    else:
        return True


data = [rock, paper, scissors]
print("Welcome to Rock, Paper and Scissors game!")

while True:
    print("What do you choose? Type 1 for 'Rock', 2 for 'Paper' and 3 for 'Scissors'")
    user_input = int(input()) - 1
    computer_input = random.randint(0, 2)

    print(data[user_input])
    print("\n")
    print("Computer Choose")
    print(data[computer_input])

    if user_input == computer_input:
        print("Its a draw!")
    else:
        ans = resultA(user_input, computer_input)
        if ans == True:
            print("You won!")
        else:
            print("You loose!")

    print("Do you want to try again? Type 'y' for yes and 'n' for no")
    try_again = input().lower()
    if try_again == 'n':
        break
