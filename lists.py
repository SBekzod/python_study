spe_list = [1, 3, 4, 5, 9, 3, 8]
ele_max = max(spe_list)
ele_min = min(spe_list)

ele_count = spe_list.count(3)

print('In the list, the maximum value is {0} and minimum value is {1}'.format(ele_max, ele_min))
print('counts of 3 in list equals {0}'.format(ele_count))

even = [2, 4, 8, 12, 20]
odd = [1, 3, 7, 11, 25]
numbers = even + odd
# numbers.sort()
numbers = sorted(numbers)
print('The numbers equal to the list of {0}'.format(numbers))


