import random
'''
Rules:
Rock = 0
paper = -1
scissor = 1
'''
print("Welcome to Rock, Paper, Scissor Game!")
print("You have to choose one option of the following")
print("Rock = 0")
print("Paper = -1")
print("Scissor = 1")

youDict = {0: "Rock", -1: "Paper", 1: "Scissor"}
reverseDict = {"Rock": 0, "Paper": -1, "Scissor": 1}

def play_round(You):
    # computer must be able to pick 0 also
    computer = random.choice([-1, 0, 1])
    # validate user input
    if You not in youDict:
        print("Userinput is invalid")
        return "invalid"  # counts as a played round but invalid
    you = youDict[You]
    print(f"You choose {you}\nComputer choose {youDict[computer]}")

    if computer == You:
        print("It's a Tie!")
        return "tie"

    else:
        if computer == -1 and You == 1: # (-1)-(1)) = -2
            print("You Win!")
            return "user"

        elif computer == 0 and You == -1: # (0 -(-1)) = 1
            print("You Wins!")
            return "user"
        
        elif computer == 1 and You == 0: # 1-0 = 1
            print("You Wins!")
            return "user"

        elif computer == 1 and You == -1: # (1)-(-1)) = 2
            print("computer Wins!")
            return "computer"
        
        elif computer == -1 and You == 0: # ((-1)-0)= -1
            print("computer Wins!")
            return "computer"

        elif computer == 0 and You == 1: #(0-1)= -1
            print("computer Wins!")
            return "computer"

        else:
            print("Userinput is invalid")
            return "invalid"

# Play n no.of rounds and count results
user_wins = 0
computer_wins = 0
ties = 0
invalids = 0

for i in range(1, 20):
    try:
        You = int(input(f"Round {i} - Enter your choice (0, -1, 1): "))
    except ValueError:
        print("Userinput is invalid")
        invalids += 1
        continue

    result = play_round(You)
    if result == "user":
        user_wins += 1
    elif result == "computer":
        computer_wins += 1
    elif result == "tie":
        ties += 1
    else:
        invalids += 1

# Final summary
print("\n--- Game Over ---")
print(f"Your wins   : {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Ties         : {ties}")
print(f"Invalid inputs: {invalids}")

if user_wins > computer_wins:
    print("Overall Winner: You!")
elif computer_wins > user_wins:
    print("Overall Winner: Computer!")
else:
    print("Overall Result: Draw!")
