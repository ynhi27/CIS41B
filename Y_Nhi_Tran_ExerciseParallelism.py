# Y Nhi Tran
# Exercise Parallelism

import multiprocessing
import time


class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name


# Create multiprocessing Values for shared balances
account1_balance = multiprocessing.Value('i', 100)
account2_balance = multiprocessing.Value('i', 0)


class BankTransferProcess(multiprocessing.Process):
    def __init__(self, sender_balance, receiver_balance, amount):
        multiprocessing.Process.__init__(self)
        self.sender_balance = sender_balance
        self.receiver_balance = receiver_balance
        self.amount = amount

    def run(self):
        with self.sender_balance.get_lock():
            sender_initial_balance = self.sender_balance.value
            sender_initial_balance -= self.amount
            # Inserting delay to allow switch between processes
            time.sleep(0.001)
            self.sender_balance.value = sender_initial_balance

        with self.receiver_balance.get_lock():
            receiver_initial_balance = self.receiver_balance.value
            receiver_initial_balance += self.amount
            # Inserting delay to allow switch between processes
            time.sleep(0.001)
            self.receiver_balance.value = receiver_initial_balance


if __name__ == "__main__":
    processes = []

    for i in range(account1_balance.value):
        processes.append(BankTransferProcess(account1_balance, account2_balance, 1))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(account1_balance.value)
    print(account2_balance.value)

