print('********************************')

range_1 = range(0, 10)
list_1 = list(range_1)
print('the range till 10')
print(list_1)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print('even list')
print(even)
print('odd list')
print(odd)

try:
    print('********************************')
    print('find {0} in even list'.format(4))
    print(even.index(4))
    print('find {0} in odd list'.format(3))
    print(odd.index(3))
    print('find {0} in odd list'.format(4))
    target = odd.index(4)
    print(target)

    if target is BaseException():
        raise target

except BaseException as err:
    print('ERROR: ', err)





