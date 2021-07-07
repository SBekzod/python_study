print('\n\n**** STRINGS ****')
# TESTING INDEX AND THE VALUE OF THE APPROPRIATE INDEX
str = 'abscdjfsdifjsdkfgf'
index = str.index('d')
target = str[int('{0}'.format(index))]
print('The string is {0} and the target index is {1} and targeted char is {2}'.format(str, index, target))

# REVERSE THE STRING
new_str = 'egaugnal lufrewop dna gnorts si nohtyp'
print(new_str[::-1])

print('\n\n**** RANGE ****')
# THREE FEATURED RANGES
hundreds_range = range(0, 100)
my_target = hundreds_range[::2]
for ele in my_target:
    print('{0}\t'.format(ele), end='')
else:
    print('')
    print('THE LIST IS CHECKED')
print(my_target.index(50))

print('\n\n**** TUPLE ****')
my_tuple = 'martin', 32, 'uzbek', 'married', True
print('this is my_tuple: {0}'.format(my_tuple))
print('this is my_tuple[0]: {0}'.format(my_tuple[0]))
