from time import sleep
print('file name __name__ :', __name__)
print('Testing Functions on Python file')


def count_till_ten(*par, separate=":", end='', file=None, flush=False):
    print(par)
    for i in range(1, 11):
        print(i, separate)
        sleep(1)


# controls and commutes if the source is run inside
if __name__ == '__main__':
    count_till_ten('function is started', "you")
    print('PERFECT')
