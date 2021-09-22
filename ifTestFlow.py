person = 'Morgan'
animal = 'lion'
while True:
    letter = input('Please enter just one letter: ')
    if letter in animal:
        print('Letter {0} is inside of the name of animal variable'.format(letter))
    elif letter in person:
        print('Letter {0} is inside of the name of person variable'.format(letter))
    else:
        print('NONE of {0} here'.format(letter))


