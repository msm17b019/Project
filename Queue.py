from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.line=deque()

    def enqueue(self,value):
        self.line.appendleft(value)

    def dequeue(self):
        if len(self.line)==0:
            print('Order finished....')
            return
        return self.line.pop()

    def size(self):
        return len(self.line)

    def is_empty(self):
        return len(self.line)==0

food_order_queue=Queue()

def place_order(orders):
    for order in orders:
        print('Placing order for: ',order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
        order=food_order_queue.dequeue()
        if order==None:
            break
        print('Now serving: ',order)
        time.sleep(2)


if __name__=='__main__':
    orders=['pizza','Masala paneer','tandoori roti','naan']
    t1=threading.Thread(target=place_order,args=(orders,))
    t2=threading.Thread(target=serve_order)

    t1.start()
    t2.start()