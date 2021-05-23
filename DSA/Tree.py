class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        spaces=' ' * self.get_level() * 3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root=TreeNode('Electronics')
    
    laptop=TreeNode('Laptop')
    root.add_child(laptop)
    mac=TreeNode('MacBook')
    ms=TreeNode('Microsoft')
    think=TreeNode('ThinkPad')
    laptop.add_child(mac)
    laptop.add_child(mac)
    laptop.add_child(think)

    cellphone=TreeNode('Cell Phones')
    root.add_child(cellphone)
    iphone=TreeNode('Iphones')
    google=TreeNode('Google Pixel')
    vivo=TreeNode('Vivo')
    cellphone.add_child(iphone)
    cellphone.add_child(google)
    cellphone.add_child(vivo)

    tv=TreeNode('Televisions')
    root.add_child(tv)
    sam=TreeNode('Samsung')
    lg=TreeNode('LG')
    tv.add_child(sam)
    tv.add_child(lg)

    return root

if __name__=='__main__':
    root = build_product_tree()
    root.print_tree()
    pass