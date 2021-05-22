from collections import deque

class Queue:
    def __init__(self):
        self.line=deque()

    def enqueue(self,value):
        self.line.appendleft(value)

    def dequeue(self):
        if len(self.line)==0:
            return "Queue is empty"
        return self.line.pop()

    def add_front(self):
        return self.line[-1]

    def size(self):
        return len(self.line)

    def is_empty(self):
        return len(self.line)==0

def print_binary(start,end):
    s=str(bin(start).lstrip('0b'))
    n=(end-start)+1
    q=Queue()
    q.enqueue(s)
    for i in range(n):
        a=q.add_front()
        q.enqueue(a+'0')
        q.enqueue(a+'1')
        print(q.dequeue())

if __name__=='__main__':
    print_binary(1,10)