from concurrent import futures
from threading import Lock, Thread
import time

a = 5
b = 5

a_lock = Lock()
b_lock = Lock()


def thread1calc():
    global a
    global b

    print('aquire resource a')
    a_lock.acquire()
    time.sleep(5)

    print('acquire resource b')
    b_lock.acquire()
    time.sleep(5)

    a += 5
    b += 5

    print('release resources')
    a_lock.release()
    b_lock.release()


def thread2calc():
    global a
    global b

    print('aquire resource b')
    b_lock.acquire()
    time.sleep(5)

    print('acquire resource a')
    a_lock.acquire()
    time.sleep(5)

    a += 10
    b += 10

    print('release resources')
    b_lock.release()
    a_lock.release()


if __name__ == '__main__':
    print('main')

    t1 = Thread(target=thread1calc)
    t1.start()

    t2 = Thread(target=thread2calc)
    t2.start()