class HashMap:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash%self.max

    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for idx,item in enumerate(self.arr[h]):  #To update the value of key in list if key already exists
            if len(item)==2 and item[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
                break

        if not found:                            #Add value of key if key don't exist in list.
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for item in self.arr[h]:
            if item[0]==key:
                return item[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,item in enumerate(self.arr[h]):
                if item[0]==key:
                    del self.arr[h][index]


if __name__=='__main__':
    t=HashMap()
    t['March 7']=120
    t['March 9']=14
    t['March 24']=117
    t['March 6']=34
    t['March 17']=68
    t['March 7']=82
    t['March 17']=89
    print(t.arr)
    print(t['March 24'])
    del t['March 17']
    print(t.arr)