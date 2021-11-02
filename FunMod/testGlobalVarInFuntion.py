from time import sleep

print('Testing Functions on Python')
named = {'surname': 'hero'}
person = 1
animal = 3

def count_till_ten(*par, separated=":", end='', file=None, flush=False):
    print(par)
    print(named['surname'])
    named['surname'] = 'not hero'

    print(person)

    animal = 4
    print(animal)

    for i in range(1, 11):
        print(i, separated)
        sleep(1)


count_till_ten('function is started', "you")
print(named['surname'])
print(animal)
