import random

user_win = 0
computer_win = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("type rock/paper/scissors or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    #rock: 0, paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print("computer picked %s " %computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_win += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_win += 1
    elif user_input == "scissors" and computer_pick == "rock":
        print("you won!")
        user_win += 1
    elif user_input == "rock" and computer_pick == "paper":
        print("you won!")
        user_win += 1
    elif user_input == "paper" and computer_pick == "scissors":
        print("you won!")
        user_win += 1
    else:
        print("computer won!")
        computer_win += 1
    
print("you won %s times" %user_win)
print("computer won %s times" %computer_win)
print("good bye!")
