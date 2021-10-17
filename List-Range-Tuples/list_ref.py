list_1 = [1, 9, 5, 7]
list_1.sort(reverse=True)  # ins.sort(): mutates the list_1

list_2 = sorted(list_1)    # sorted(ins): creates and returns completely sorted new list with new reference
print(list_1)              # [9, 7, 5, 1]
print(list_2)              # [1, 5, 7, 9]
print(list_1 is list_2)    # False

list_3 = list(list_1)      # list(ins): creates and returns completely new list
print(list_3)              # [9, 7, 5, 1]
print(list_1 is list_3)    # False

