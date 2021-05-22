'''
Exercise - 1
Author - Sujeet Kumar
'''

class HashMap:
    def __init__(self):
        self.max=7
        self.arr=[[] for i in range(self.max)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash%self.max

    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found=False
        for index,item in enumerate(self.arr[h]):
            if item[0]==key and len(item)==2:
                self.arr[h][index]=(key,value)
                found=True
                break

        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for item in self.arr[h]:
            if item[0]==key:
                return item[1]

    def get_avg(self,days):  
        total=0
        for i in range(1,days+1):
            total+=self.__getitem__('Jan'+' '+str(i))
        print(total/days)

    def get_max(self,days_from_start):   
        l=[]
        for i in range(days_from_start):
            l.append(self.__getitem__('Jan'+' '+str(i+1)))

        print(max(l))

    def get_temp_on_date(self,date):    # Temp on particular date
        print(self.__getitem__(date))

if __name__=='__main__':
    t=HashMap()
    with open("C:\\Users\\sujee\\Downloads\\data-structures-algorithms-python-master\\data_structures\\4_HashTable_2_Collisions\\Solution\\nyc_weather.csv","r") as f:
        a=f.readlines()
        for idx,item in enumerate(a):
            if idx>=1:
                a,b=map(str,item.rstrip('\n').split(','))
                b=int(b)
                t[a]=b
    print(t.arr)
    t.get_avg(7)
    t.get_max(10)
    t.get_temp_on_date('Jan 4')
    t.get_temp_on_date('Jan 9')
    # print(t['Jan 4'])
    # print(t['Jan 9'])