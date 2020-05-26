from concurrent import futures
from threading import Lock


class BankAccount:
    def __init__(self):
        self.balance = 100
        self.lock_obj = Lock()

    def update(self, transaction, amount):
        print(f'{transaction} started')

        with self.lock_obj:
            self.tmp_amount = self.balance
            self.tmp_amount += amount
            self.balance = self.tmp_amount

        print(f'{transaction} ended')


if __name__ == '__main__':
    print(' main started ')
    account = BankAccount()

    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(account.update, ('refill', 'withdraw'), (100, -200))

    print(f'finished main acc balance = {account.balance}')