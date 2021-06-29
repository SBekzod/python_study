import random

highest = 10
answer = random.randint(1, highest)
# print('here is the answer {0} given!'.format(answer))

print('GAME IS STARTED')
guess = 0
times = 0
total_attempts = 0

while answer != guess and times < 3:
    try:
        guess = int(input('Please guess any numbers between 0 and {}: '.format(highest)))
        total_attempts = total_attempts + 1
        if guess > answer:
            print('please guess less number than {0}'.format(guess))
        elif guess < answer:
            print('please guess higher number than {0}'.format(guess))
        else:
            print('CONGRATULATION YOU GUESSED {0}!'.format(answer))
            times = times + 1
            answer = random.randint(1, highest)
            guess = 0
    except:
        print('error => enter only numbers')
        guess = 0
else:
    print('GAME IS OVER, your statistics: game completed successfully with attempts {0}'.format(total_attempts))

