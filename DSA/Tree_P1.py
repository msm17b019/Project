class Tree:
    def __init__(self,name,designation):
        self.name=name 
        self.designation=designation
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

    def print_tree_name(self):
        spaces=' ' * self.get_level() * 3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.name)
        if len(self.children):
            for child in self.children:
                child.print_tree_name()

    def print_tree_designation(self):
        spaces=' ' * self.get_level() * 3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.designation)
        if len(self.children):
            for child in self.children:
                child.print_tree_designation()

    def print_tree(self):
        spaces=' ' * self.get_level() * 3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.name + '  ('+self.designation+')')
        if len(self.children):
            for child in self.children:
                child.print_tree()



def build_company_tree():
    root=Tree('Nilupul','CEO')
    e11=Tree('Chinmay','CTO')
    root.add_child(e11)
    e12=Tree('Gels','HR Head')
    root.add_child(e12)
    e21=Tree('Vishwa','Infrastructure Head')
    e11.add_child(e21)
    e22=Tree('Aamir','Application Head')
    e11.add_child(e22)
    e23=Tree('Peter','Recruitment Manager')
    e12.add_child(e23)
    e24=Tree('Waqas','Policy Manager')
    e12.add_child(e24)

    e31=Tree('Dhaval','Cloud Manager')
    e21.add_child(e31)
    e32=Tree('Abhijit','App Manager')
    e21.add_child(e32)

    return root

if __name__=='__main__':
    root=build_company_tree()
    root.print_tree_name()
    root.print_tree_designation()
    root.print_tree()
    pass