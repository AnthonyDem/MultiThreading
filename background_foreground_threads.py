import threading


def read_ints(path):
    lst = []
    with open(path, 'r') as f:
        while f:
            line = f.readline()
            lst.append(int(line))
    return lst


def count_three_sum(ints):
    print('started counter')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'triple found : {ints[i]}, {ints[j]}, {ints[k]}')
    print(' ended count three sum')


if __name__=='__main__':
    print(' started main thread ')
    ints = read_ints('..\\data\\ints.txt')
    t = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    t.start()

    count_three_sum(ints)
    print(input('what are you waiting for?'))

    t.join()

    print('ended main thread')