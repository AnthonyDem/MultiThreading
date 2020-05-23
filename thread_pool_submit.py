from concurrent import futures
import time


def div(divizor, limit):
    result = 0

    for i in range(1, limit):
        if i % divizor == 0:
            result += i
        time.sleep(0.2)
    print(f'ended divizor {divizor}', end='\n')
    return  result


if __name__=='__main__':
    print('started main')
    future = []
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        future.append(executor.submit(div, 3, 30))
        future.append(executor.submit(div, 4, 40))

        while future[0].running() and future[1].running():
            print('.', end='')
            time.sleep(1)

        for f in future:
            print(f'{f.result()}')

        print('After with block')
