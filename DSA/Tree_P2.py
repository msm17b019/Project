class Node:
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

    def print_tree(self,num):
        spaces=' ' * self.get_level() * 3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)

        if self.get_level()<num:
            for child in self.children:
                child.print_tree(num)


def build_location_tree():
    root=Node('Global')
    ind=Node('India')
    root.add_child(ind)
    us=Node('USA')
    root.add_child(us)
    guj=Node('Gujarat')
    ind.add_child(guj)
    kar=Node('Karnataka')
    ind.add_child(kar)
    ahm=Node('Ahmedabad')
    guj.add_child(ahm)
    bar=Node('Baroda')
    guj.add_child(bar)
    ban=Node('Bangalore')
    kar.add_child(ban)
    my=Node('Mysore')
    kar.add_child(my)

    new=Node('New Jersey')
    us.add_child(new)
    prince=Node('Princeton')
    new.add_child(prince)
    trent=Node('Trenton')
    new.add_child(trent)
    
    cal=Node('California')
    us.add_child(cal)
    san=Node('San Francisco')
    cal.add_child(san)
    mount=Node('Mountain View')
    cal.add_child(mount)
    pal=Node('Palo Alto')
    cal.add_child(pal)

    return root

if __name__=="__main__":
    root=build_location_tree()
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)
    pass


