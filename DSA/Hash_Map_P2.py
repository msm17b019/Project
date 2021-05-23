'''
Exercise -2
'''

word_count={}
with open("C:\\Users\\sujee\\Downloads\\data-structures-algorithms-python-master\\data_structures\\4_HashTable_2_Collisions\\Solution\\poem.txt","r") as f:
    for line in f:
        tokens=line.split(' ')
        for token in tokens:
            token=token.replace('\n','')

            if token in word_count:
                word_count[token]+=1

            else:
                word_count[token]=1

print(word_count)