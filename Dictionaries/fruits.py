fruits = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'green'}
print('THE FRUITS ONE:')
print(fruits)

# fruits['orange'] = 'orange'
# print('THE FRUITS TWO:')
# print(fruits)
#
# del fruits['apple']
# print('THE FRUITS THREE:')
# print(fruits)
#
# fruits.clear()
# print('THE FRUITS FOUR:')
# print(fruits)

while True:
    search = input('Type the fruit name here: ')
    if search == 'quit':
        break
    # if search in fruits:
    #     result = fruits.get(search)
    #     print(result)
    # else:
    #     print('There is no fruit like than on fruits dictionary')
    result = fruits.get(search, 'we do not have this fruit inside of our dictionary')
    print(result)







