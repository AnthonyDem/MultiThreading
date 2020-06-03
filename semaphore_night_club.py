import threading
import time


class Club:
    def __init__(self):
        self.bouncer = threading.Semaphore(3)

    def open_club(self):
        for x in range(51):
            t = threading.Thread(target=self.guest, args=[x])
            t.start()

    def guest(self, guest_id):
        print(f'Guest {guest_id} is waiting night club ')
        self.bouncer.acquire()

        print(f'\nGuest {guest_id} is dancing')
        time.sleep(1)

        print(f'\nGuest {guest_id} is leaving the club')
        self.bouncer.release()


if __name__ ==  '__main__':
    club = Club()
    club.open_club()