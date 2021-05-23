class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class Double_linked_list:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        if self.head is None:
            node=Node(data,self.head,None)
            self.head=node
            return
        node=Node(data,self.head,None)
        self.head.prev=node
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None,itr)

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self,data_after,data_to_insert):
        if self.head.data==data_after:
            node=Node(data_to_insert,self.head.next,self.head)
            self.head.next=node
            self.head.next.next.prev=node
            return

        itr=self.head
        while itr.next:
            if itr.next.data==data_after:
                node=Node(data_to_insert,itr.next.next,itr.next)
                itr.next.next=node
                itr.next.next.next.prev=node
                return
            itr=itr.next

    def remove_by_values(self,data_to_be_removed):
        if self.head.data==data_to_be_removed:
            self.head=self.head.next
            self.head.prev=None
            return

        itr=self.head
        while itr.next:
            if itr.next.data==data_to_be_removed:
                itr.next.next.prev=itr.next.prev
                itr.next.prev.next=itr.next.next
                return

            itr=itr.next

    def get_length(self):
        if self.head is None:
            return 
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_at(self,index,data):
        if index<0 or index>self.get_length()-1:
            raise Exception('Invalid index')

        if index==0:
            self.insert_at_beginning(data)
            return

        count=0
        itr=self.head
        while itr:
            count+=1
            if index==count:
                node=Node(data,itr.next,itr)
                itr.next=node
                itr.next.next.prev=node
                return
            itr=itr.next

    
    def remove_at(self,index):
        if index<0 or index>self.get_length()-1:
            raise Exception('Invalid index')

        if index==0:
            self.head=self.head.next
            self.head.prev=None
            return

        itr=self.head
        count=0
        while itr:
            count+=1
            if count==index:
                itr.next=itr.next.next
                itr.next.prev=itr
                return
            itr=itr.next

    def print_forward(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data)+'<--->'
            itr=itr.next
        print(listr)

    def print_backward(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr=self.head
        listr=''
        while itr.next:
            itr=itr.next

        while itr:
            listr+=str(itr.data)+'<--->'
            itr=itr.prev
        print(listr)    

if __name__=='__main__':
    dll=Double_linked_list()
    dll.insert_values([8,7,5,39])
    dll.insert_at_beginning(21)
    dll.insert_at_beginning(23)
    dll.insert_at_end(3)
    dll.insert_at_beginning(1)
    dll.insert_at_end(9)
    dll.insert_at(4,56)
    dll.remove_at(3)
    dll.insert_after_value(21,15)
    dll.remove_by_values(7)
    dll.print_forward()
    dll.print_backward()
    print(dll.get_length())