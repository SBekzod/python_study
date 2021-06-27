
# transforming text into number
number = '9,450,545,545'
clean_number = ''

for char in number:
    if char in '0123456789':
        clean_number += char

new_numb = int(clean_number)
print('New number equal to {0}'.format(new_numb))

# using array instead of range
for state in ['hello', 'hi', 'how do you do?']:
    print('The state equals to : {0}'.format(state))

# three parametric range is used
for i in range(0, 100, 5):
    print('This is i: {0}'.format(i))

# nested for loops on action
for i in range(0, 10):
    for k in range(0, 10):
        print('Numbers {0} * {1} equals to {2}'.format(i, k, i*k))
    print('-----------------')
