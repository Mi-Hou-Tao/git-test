import random

gesture_choices = ['Rock','Paper','Scissors']

print("(type 'q' to quit)")

Rock_count = 0
Paper_count = 0
Scissors_count = 0
round_count = 0
user_wins = 0
machine_wins = 0

last_throw = None

patterns = {
    'Rock': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
    'Paper': {'Rock': 0, 'Paper': 0, 'Scissors': 0},
    'Scissors': {'Rock': 0, 'Paper': 0, 'Scissors': 0}
}

while True:

    user_throw = input("What's your throw?Rock/Paper/Scissors\n")
    if user_throw == 'q':
        break    
    if user_throw not in gesture_choices:
        print('Invalid throw.')
        continue
    last_throw = user_throw

    if user_throw =='Rock':
        Rock_count += 1
    elif user_throw =='Paper':
        Paper_count += 1
    else:
        Scissors_count += 1

    
    
    next_counts = patterns[last_throw]    
    total = sum(next_counts.values())

    if total < 4:
        machine_throw = random.choice(gesture_choices)
    elif random.random() < 0.7:

            
        prediction = max(next_counts,key=next_counts.get)
        if prediction == 'Rock':
            machine_throw = 'Paper'
        elif prediction == 'Paper':
            machine_throw = 'Scissors'
        else:
            machine_throw = 'Rock'
    else:
            machine_throw = random.choice(gesture_choices)

    

    print('you:',user_throw)
    print('me:',machine_throw)


    if (user_throw == 'Rock' and machine_throw == 'Scissors') or \
    (user_throw == 'Paper' and machine_throw == 'Rock') or \
    (user_throw == 'Scissors' and machine_throw == 'Paper'):
        print('You win.')
        user_wins += 1
    elif user_throw == machine_throw:
        print('We drew.')
    else:
        print('I won.')
        machine_wins += 1

    round_count += 1

    if last_throw is not None:
        patterns[last_throw][user_throw] += 1
    last_throw = user_throw

    


print('=============Game Summary=============')
print('round count: ',round_count)
print('Your wins: ',user_wins)
print('Machine wins:',machine_wins)

if round_count > 0:
    print('Your win rate: ',user_wins / round_count * 100,'%')
    print('Machine win rate: ',machine_wins / round_count * 100,'%')




        


