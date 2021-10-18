my_tuple = 'martin', 33, 'married', True
my_list = ['martin', 33, 'married', True]

my_list.insert(0, '1')
my_list.append('uzbek')

print('This is tuple: {0}'.format(my_tuple))
print('This is a list: {0}'.format(my_list))

name, year, state, status = my_tuple
print(name)
print(year)
