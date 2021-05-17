class Node:
    def __init__(self,data,label):
        self.data=data
        self.label=label
        self.children=[]

    def add_child(self,num1,num2):
        if self.data==num1:
            self.children.append(Node(num2,0))

        else:
            if len(self.children):
                for item in self.children:
                    item.add_child(num1,num2)

    def get_total(self,total,m):   # Total number of nodes in sub-tree
        if len(self.children):
            for item in self.children:
                item.get_total(total,m)
                total+=1
                m.append(total)
                total=0
        if sum(m)==0:
            return 0
        else:    
            return sum(m)

    def get_height(self,height,m):  # Height of node in tree
        if len(self.children):
            for item in self.children:
                height+=1
                item.get_height(height,m)
                m.append(height)
                
            if len(m)==0:
                return 0
            else:
                return max(m)


if __name__=='__main__':
    t=int(input())
    while t>0:
        n,x=map(int,input().split())
        u,v=map(int,input().split())
        root=Node(u,x)
        root.add_child(u,v)
        for i in range(1,n-1):
            n1,n2=map(int,input().split())
            root.add_child(n1,n2)
        
        # print(root.get_total(0,[]))
        # print(root.get_height(0,[]))
        t-=1