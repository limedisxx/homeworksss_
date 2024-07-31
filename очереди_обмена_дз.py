import threading
import queue
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(threading.Thread):
    def __init__(self, cafe, customer_id):
        super().__init__()
        self.cafe = cafe
        self.customer_id = customer_id

    def run(self):
        self.cafe.serve_customer(self)

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customer_id = 0
        self.lock = threading.Lock()

    def customer_arrival(self):
        for _ in range(20):
            self.customer_id += 1
            customer = Customer(self, self.customer_id)
            print(f"Посетитель номер {self.customer_id} прибыл.")
            self.queue.put(customer)
            customer.start()
            time.sleep(1)

    def serve_customer(self, customer):
        while True:
            with self.lock:
                free_table = None
                for table in self.tables:
                    if not table.is_busy:
                        free_table = table
                        break
                if free_table:
                    free_table.is_busy = True
                    print(f"Посетитель номер {customer.customer_id} сел за стол {free_table.number}.")
                    time.sleep(5)
                    print(f"Посетитель номер {customer.customer_id} покушал и ушёл.")
                    free_table.is_busy = False
                    break
                else:
                    print(f"Посетитель номер {customer.customer_id} ожидает свободный стол.")
            time.sleep(1)

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
