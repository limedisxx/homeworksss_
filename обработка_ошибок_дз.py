import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Depositing {amount}")
            self.balance += amount
            print(f"New balance after deposit: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}")
                self.balance -= amount
                print(f"New balance after withdrawal: {self.balance}")
            else:
                print(f"Insufficient funds to withdraw {amount}. Current balance: {self.balance}")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

if __name__ == "__main__":
    account = BankAccount()

    deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()

    print(f"Final balance: {account.balance}")