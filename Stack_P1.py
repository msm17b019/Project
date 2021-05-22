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

def is_balanced(value):
    s=Stack()
    for char in value:
        s.push(char)
    b1=0
    b2=0
    b3=0
    b4=0
    b5=0
    b6=0
    for i in range(s.size()):
        a=s.pop()
        if a=='(':
            b1+=1
        if a==')':
            b2+=1
        if a=='[':
            b3+=1
        if a==']':
            b4+=1
        if a=='{':
            b5+=1
        if a=='}':
            b6+=1

    if b1==b2 and b3==b4 and b5==b6:
        print('True')
    else:
        print('False')

if __name__=='__main__':
    is_balanced('()')