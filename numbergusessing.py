import random
print('Welcome to Number Guessing Game!')
secret = random.randint(1, 100)
attempts = 0
while True:
    try:
        guess = int(input('Enter your guess (1-100): '))
        attempts += 1
        if guess < secret:
            print('Too Low!')
        elif guess > secret:
            print('Too High!')
        else:
            print(f'Correct! You guessed in {attempts} attempts.')
            break
    except ValueError:
        print('Please enter a valid number.')