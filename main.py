import random
import time

player =  None
running = True
player_lives = 3
computer_lives = 3
while True:
    list = ["rock", "paper", "scissors"]
    computer = random.choice(list)
    player = input("Choose rock,paper Or scissors:")
    while player not in list:
        player = input("I Said Choose Rock,Paper Or Scissors:")

    print(f"Player: {player}")
    time.sleep(0.5)
    print(f'Computer: {computer}')
    time.sleep(0.5)
    if player == computer:
        time.sleep(0.5)
        print("It's a tie")
        time.sleep(0.5)
        print(f"Computer Lives: {computer_lives} | Player Lives: {player_lives}")
        time.sleep(0.5)
    elif player == "rock" and computer == "paper":
        time.sleep(0.5)
        print("You Loose")
        player_lives -=1
        time.sleep(0.5)
        print(f"Computer Lives: {computer_lives} | Player Lives: {player_lives}")
        if player_lives == 0:
            time.sleep(0.5)
            print("You're Out Of Lives,Computer Wins!")
            break
    elif player == "paper" and computer == "scissors":
        time.sleep(0.5)
        print("You Loose")
        player_lives -= 1
        time.sleep(0.5)
        print(f"Computer Lives: {computer_lives} | Player Lives: {player_lives}")
        if player_lives == 0:
            time.sleep(0.5)
            print("You're Out Of Lives,Computer Wins!")
            break
    elif player == "scissors" and computer == "rock":
        time.sleep(0.5)
        print("You Loose")
        player_lives -= 1
        time.sleep(0.5)
        print(f"Computer Lives: {computer_lives} | Player Lives: {player_lives}")
        if player_lives == 0:
            time.sleep(0.5)
            print("You're Out Of Lives,Computer Wins!")
            break
    else:
        time.sleep(0.5)
        print("You Win")
        computer_lives -=1
        time.sleep(0.5)
        print(f"Computer Lives: {computer_lives} | Player Lives: {player_lives}")
        if computer_lives == 0:
            time.sleep(0.5)
            print("Computer Is Out Of Lives,You Win!")
            time.sleep(0.5)
            break
print("Thanks For Playing!")




