import random

roll =0
count = 0

print('First Person to roll a 5 wins')

while roll != 5:
        name = input('Enter a name, or \'q\' to quit:   ')

        if name.strip() == '':
            continue

        if name == 'q':
            break

        count = count + 1
        roll = random.randint(1, 5)
        print(f'{name} rolled {roll}')
else:
        print(f'{name} wins!')
print(f'you rolled the dice {count} times')