import random

gesture_choices = ['Rock','Paper','Scissors']

print("(type 'q' to quit)")
while True:
    user_throw = input("What's your throw?Rock/Paper/Scissors\n")
    if user_throw == 'q':
        break
    if user_throw not in gesture_choices:
        print('Invalid throw.')
        continue
    machine_throw = random.choice(gesture_choices)

    print('you:',user_throw)
    print('me:',machine_throw)

    if (user_throw == 'Rock' and machine_throw == 'Scissors') or \
    (user_throw == 'Paper' and machine_throw == 'Rock') or \
    (user_throw == 'Scissors' and machine_throw == 'Paper'):
        print('You win.')
    elif user_throw == machine_throw:
        print('We drew.')
    else:
        print('I won.')

        


