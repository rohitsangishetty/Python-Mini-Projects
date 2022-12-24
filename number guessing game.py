import random

top_of_range = input('Type a number to be the upper limit for the game: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range) #range for the random number, which is 0 to top_of_range
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess:')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print('Congratulations! You guessed the number!')
        break
    elif user_guess > random_number:
            print('You guessed above the number. Try again!')
    else: 
        user_guess < random_number
        print('You guessed below the number. Try again!')

print(f'You won in', guesses, 'guesses!')