shop_list = ['milk', 'ham', 'pasta', 'person', 'eggs', 'bread']
for i in shop_list:
    if i == 'ham':
        continue
    if i == 'person':
        print('Please correct the shop_list, what a {0} on list'.format(i))
        break
    print('We may buy {0}'.format(i))
