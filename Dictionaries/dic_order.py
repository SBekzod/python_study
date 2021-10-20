fruits = {'lemon': 'yellow', 'apple': 'red', 'grapes': 'green', 'peach_d': 'a', 'peach_a': 'n', 'peach_a': 'ssd'}

print('THE INITIAL FRUITS')
print(fruits)

fruits_list = list(fruits.keys())
fruits_val = list(fruits.values())

fruits_list.sort()
fruits_val.sort(reverse=True)

print(fruits_list)
print(fruits_val)


