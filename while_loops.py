for i in range(0, 100):
    if i == 95:
        break
    elif i == 90:
        continue
    else:
        print('hello {0}'.format(i))

k = 0
while True:
    k = k + 1

    if k == 1000:
        break
    elif k == 995:
        continue
    else:
        print('Hello {0}'.format(k))
