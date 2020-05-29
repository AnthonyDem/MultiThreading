from enum import Enum
import threading
import random
import time


class Event:
    def __init__(self):
        self.__handlers = []

    def __call__(self, *args, **kwargs):
        for handler in self.__handlers:
            handler(*args, **kwargs)

    def __iadd__(self, other):
        self.__handlers.append(other)
        return self

    def __isub__(self, other):
        self.__handlers.remove(other)


class OperatioStatus(Enum):
    FINISHED = 1
    FAULTED = 0


class Protocol:
    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address

        self.message_received = Event()

        self.set_ip_port()

    def set_ip_port(self):
        print('set ip and port')
        time.sleep(0.2)
        return self

    def send(self, op_code, param):
        def process_sending():
            print(f'operation in process with param {param}')
            result = self.process(op_code, param)
            self.message_received(result)

        t = threading.Thread(target=process_sending())
        t.start()

    def process(self, op_code, param):
        print(f'process started with code {op_code} and params {param}')
        time.sleep(1)

        finished = random.randint(0, 1) == 1
        return OperatioStatus.FINISHED if finished else OperatioStatus.FAULTED


class BankTerminal:
    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address
        self.protocol = Protocol(port, ip_address)
        self.protocol.message_received += self.on_message_received

        self.operation_signal = threading.Event()

    def on_message_received(self, status):
        print(f'signal for event {status}')
        self.operation_signal.set()

    def purchase(self, amount):
        def process_purchase():
            purchase_op_code = 1
            self.protocol.send(purchase_op_code, amount)
            self.operation_signal.clear()
            print('\nWaiting for ')
            self.operation_signal.wait()
            print('purchase finished ')

        t = threading.Thread(target=process_purchase)
        t.start()
        return t


if __name__ == '__main__':
    bt = BankTerminal(10, '192.160.0.1')
    t = bt.purchase(20)
    print('Main decided to wait for purchase 1')
    t.join()
    t = bt.purchase(10)
    print('Main decided to wait for purchase 2')
    t.join()