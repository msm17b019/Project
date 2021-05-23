class HashMap:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash%self.max

    def update(self,key,value):
        for item in self.arr:
            if item !=None:
                if item[0]==key:
                    item[1]=value
                    return

    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=True
        if None in self.arr:
            while found:
                if self.arr[h] is None:
                    self.arr[h]=[key,value]
                    found=False
                h=(h+1)%self.max

        else:
            raise Exception('Hash Map is Full')

    def __getitem__(self,key):
        h=self.get_hash(key)
        if self.arr[h] is None:
            return 
        
        for item in self.arr:
            if len(item)==2:
                if item[0]==key:
                    print(item[1])

    def delete(self,key):
        for item in self.arr:
            if item != None:
                if item[0]==key:
                    item.clear()
                    return

if __name__=='__main__':
    t=HashMap()
    t['Raj']=23
    t['Rahul']=43
    t['Sujeet']=27
    t['Soni']=29
    t['Ram']=41
    t['Mohan']=56
    t['Rajesh']=93
    t['Rajeev']=57
    t['Karan']=53
    t['Rajveer']=49
    t.update('Sujeet',84)
    t.delete('Sujeet')
    # t['Sohail']=58  
    # t['Raj']
    print(t.arr)