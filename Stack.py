from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

def reverse_string(value):
    t=Stack()

    for char in value:
        t.push(char)

    rev_str=''

    while t.size() != 0:
        rev_str+=t.pop()

    print(rev_str)


if __name__=='__main__':
    reverse_string('We will defeat COVID-19 soon.')