class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid index')

        if index==0:
            self.head=self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid index')
        
        if index==0:
            self.insert_at_beginning(data)
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return None

        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return

        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break

            itr=itr.next

    def remove_by_values(self,data_to_be_removed):
        if self.head is None:
            return
        
        if self.head.data==data_to_be_removed:
            self.head=self.head.next
            return

        itr=self.head
        while itr.next:
            if itr.next.data==data_to_be_removed:
                itr.next=itr.next.next
                break
            itr=itr.next

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def print(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data) + '--->'
            itr=itr.next

        print(listr)


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_values([3,67,45])
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(20)
    ll.remove_at(3)
    
    ll.print()
    print(ll.get_length())