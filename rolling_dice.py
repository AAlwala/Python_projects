import random

def roll_dice():
    print("Dice Roller 🎲")
    while True:
        input("Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print("You rolled:", dice)

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    roll_dice()
