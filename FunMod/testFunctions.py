from time import sleep

print('Testing Functions on Python')


def count_till_ten(*par, separ=":", end='', file=None, flush=False):
    print(par)
    for i in range(1, 11):
        print(i, separ)
        sleep(1)


count_till_ten('function is started', "you")
