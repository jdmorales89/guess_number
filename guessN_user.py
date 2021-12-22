import random


def guess(x):
    """It asks to user to guess the a number between 0 and x.

    Args:
        x (int): Top number limit for guessing
    """
    random_number = random.randint(0, x)
    guess = -1
    while guess != random_number:
        guess = int(input(f"Guess a number between 0 and {x}: "))
        if guess < random_number:
            print("\nSorry, quess again. Too low.")
        elif guess > random_number:
            print("\nSorry, quess again. Too high.")
    print(f"\nYay, congrats. You have guessed the random number {random_number}.")


guess(10)
