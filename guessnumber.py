import random

options: int = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
running = True


print("Welcome to the Game try to guess the same number as the Ai")


while running:
    player: int = int(input("Enter a number (1-10): "))


    while player < 0 or player > 10:
        print(f"You can only  enter numbers between one and ten (1-10)!")
        player: int = int(input("Enter a number (1-10): "))

    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Ai: {computer}")

    if player == computer:
        print("You won!")
    else:
        print("You lost!")
              
        play_again: str = input("Do you want to play again? (y/n): ").lower() == "y"
        running = play_again

print("Thanks for Playing!")



