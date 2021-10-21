file = open('/Users/martin/documents/Yprojects.txt', 'r')
for line in file:
    print(line, end='')
file.close()

print("\n" * 2)
print('-' * 40)

with open('/Users/martin/documents/Yprojects.txt', 'r') as new_file:
    new_line = new_file.readline()
    while new_line:
        print(new_line, end='')
        new_line = new_file.readline()

print("\n" * 2)
print('=' * 40)

with open('/Users/martin/documents/Yprojects.txt', 'r') as new_file:
    lines = new_file.readlines()
for line in lines:
    print(line, end='')


