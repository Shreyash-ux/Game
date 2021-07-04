import random

Choice = ['Rock', 'Paper', 'Scissor']
while True:
    print("Welcome!")
    user_count = 0
    comp_count = 0
    for i in range(1, 4):
        print("Round-", i)
        print("Enter your choice : 1.Rock 2.Paper 3.Scissor = ")
        your_choice = int(input())

        if your_choice == 1:
            print("You have selected Rock")
            your_choice = 'Rock'
        elif your_choice == 2:
            print("You have selected Paper")
            your_choice = 'Paper'
        elif your_choice == 3:
            print("You have selected Scissor")
            your_choice = 'Scissor'
        else:
            print("Please correct your response")

        computer_choice = random.choice(Choice)
        print("Computer choice is ", computer_choice)

        if ((your_choice == 'Rock' and computer_choice == 'Scissor') or (
                your_choice == 'Paper' and computer_choice == 'Rock')
                or (your_choice == 'Scissor' and computer_choice == 'Paper')):
            user_count = user_count + 1
        elif ((your_choice == 'Scissor' and computer_choice == 'Rock') or (
                your_choice == 'Rock ' and computer_choice == 'Paper')
              or (your_choice == 'Paper' and computer_choice == 'Scissor')):
            comp_count = comp_count + 1

    if user_count > comp_count:
        print("You Win!")
    elif user_count < comp_count:
        print("Computer wins")
    else:
        print("Draw")
    print("Do you want to play again ? Yes or No = ")
    x = input()
    if x == 'Yes':
        continue
    else:
        break
