available_directions = ['east', 'west', 'south', 'north']

chosen_direction = input('Type the direction to go: ')
while chosen_direction not in available_directions:
    chosen_direction = input('Please choose correct direction: ')
    if chosen_direction == 'exit' or chosen_direction == 'quit':
        print('you quited')
        break
else:
    print('You are on your way to {0}, congrats bro'.format(chosen_direction))
