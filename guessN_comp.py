import random

def computer_guess(x):
    """It asks the computer to guess the a number between 0 and x.

    Args:
        x (int): Top number limit for guessing
    """
    low = 0
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'\nIs {guess} too high (H), too low (L), or correct (C)?: ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'\nYay! The computer guessed your number {guess} correctly!')

computer_guess(100)