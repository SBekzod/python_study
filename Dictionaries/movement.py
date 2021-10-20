locations = {
    0: 'you found the way to go out',
    1: 'starting point',
    2: 'you are on part B',
    3: 'you arrived on part C',
    4: 'you arrived on part D'
}

exist = [
    {},
    {'E': 3, 'W': 2, 'S': 0, 'N': 4},
    {'E': 2, 'W': 3, 'S': 2, 'N': 0},
    {'E': 4, 'W': 1, 'S': 2, 'N': 3},
    {'E': 0, 'W': 3, 'S': 2, 'N': 1}
]

loc = 1

while True:
    print('YOU ARE ON : ' + locations[loc])
    ways = ''
    for way in exist[loc]:
        ways = ways + way + ', '
    direction = input('Please choose directions: ' + ways).upper()
    loc = exist[loc][direction]

    if loc == 0:
        print('Congratulation: '+locations[0])
        break

