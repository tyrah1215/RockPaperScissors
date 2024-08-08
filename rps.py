import random 

user_wins = 0
computer_wins = 0 

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Pick Rock/Paper/Scissors or enter Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    #Assign rps to integers (r:0, p:1, s:2)
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("I picked", computer_pick + ".")

    if user_input == computer_pick:
        print("Its a tie!")

    elif user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins,".")
print("I won", computer_wins,".")

    

