from functools import wraps
import time
import threading


def mesure_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        ended = time.perf_counter() - start
    return wrap


@mesure_time
def parallel_run(ints):
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


@mesure_time
def sequentially_run(ints):
    count_three_sum(ints, 'main')
    count_three_sum(ints, 'main')


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
    print(' started main thread ')
    ints = read_ints('..\\data\\ints.txt')
    parallel_run(ints)
    sequentially_run(ints)

    print('ended main thread')
