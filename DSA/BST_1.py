class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)

    def in_order_traversal(self):
        elements=[]

        if self.left:
            elements+=self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements=[self.data]

        if self.left:
            elements+=self.left.pre_order_traversal()

        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements=[]

        if self.left:
            elements+=self.left.post_order_traversal()

        if self.right:
            elements+=self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def search(self,value):
        if self.data==value:
            return True

        if value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value>self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        
        return self.right.find_max()

    def calculate_sum(self):
        left_sum=self.left.calculate_sum() if self.left else 0 
        right_sum=self.right.calculate_sum() if self.right else 0
        return self.data+left_sum+right_sum

    def delete(self,value):
        if value<self.data:
            if self.left:
                self.left=self.left.delete(value)

        elif value>self.data:
            if self.right:
                self.right=self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_value=self.right.find_min()
            self.data=min_value

            self.right=self.right.delete(min_value)

        return self


            

def build_bst(elements):
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_bst(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(18))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    # print(numbers_tree.pre_order_traversal())
    # print(numbers_tree.post_order_traversal())
    # numbers_tree.delete(34)
    # print(numbers_tree.in_order_traversal())
