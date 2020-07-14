import random

count = 0
random = random.randint(1, 5)
guess = 0

print('Guess a number between 1 and 10')

while guess != random:
    count = count +1
    guess = input(f'Enter guess #{count}:  ')

    if guess.isnumeric() == False:
        print('Numbers oly, please!')
        continue

    guess =int(guess)

    if guess > random:
        print('Guess is too high')
    elif guess < random:
        print('Guess is too low')


print (f'You guessed in {count} times')


