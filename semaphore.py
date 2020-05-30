from concurrent import futures
import threading
import time
import random


def work(semaphore):
    time.sleep(random.randint(5, 10))
    print('releasing 1 connection')
    semaphore.release()


def connect(semaphore, reached_max_connections):
    with futures.ThreadPoolExecutor(max_workers=10) as ex:
        while True:
            connections_count = 0
            while not reached_max_connections.is_set():
                print(f'connection = {connections_count}')
                semaphore.acquire()
                connections_count += 1

                ex.submit(work, semaphore)

                time.sleep(0.8)

            time.sleep(5)


def connection_guard(semaphore, reached_max_connections):
    while True:
        print(f'[guard] semaphore = {semaphore._value}')
        time.sleep(1.5)

        if semaphore._value == 0:
            reached_max_connections.set()
            print('reached max connections ')
            time.sleep(2)
            reached_max_connections.clear()


if __name__ == '__main__':
    max_connections = 10
    reached_max_connections = threading.Event()

    semaphore = threading.Semaphore(value=max_connections)
    with futures.ThreadPoolExecutor(max_workers=2) as ex:
            ex.submit(connection_guard, semaphore, reached_max_connections)
            ex.submit(connect, semaphore, reached_max_connections)