from concurrent import futures


def read_ints(path):
    lst = []
    with open(path, 'r') as f:
        while f:
            line = f.readline()
            lst.append(int(line))
    return lst


def count_three_sum(ints, name):
    print(f'started counter in thread {name}')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'triple found in thread {name}: {ints[i]}, {ints[j]}, {ints[k]}')
    print(' ended count three sum')


if __name__ == '__main__':
    ints = read_ints('..\\data\\ints.txt')
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        threads = executor.map(count_three_sum, (ints, ints), ('t1', 't2'))
        for i in threads:
            print(f'{i}')
    print('ended main')