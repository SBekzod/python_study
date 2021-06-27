ip_address = input('Please type IP address here: ')

segment = 1
length = 0
char = ''

for char in ip_address:
    if char == '.':
        print('Segment {0} contains {1} characters'.format(segment, length))
        segment += 1
        length = 0
    else:
        length += 1
# else:
#     print('REALLY: Segment {0} contains {1} characters'.format(segment, length))

if char != '.' and char != '':
    print('Final Segment {0} contains {1} characters'.format(segment, length))
