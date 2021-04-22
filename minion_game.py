def minion_game(string):
    count1=0
    count2=0
    vowel='AEIOU'
    for i in range(len(string)):
        if string[i] not in vowel:
            count1+=(len(string)-i)
        else:
            count2+=(len(string)-i)
            
        
                
    if count1>count2:
        print('Stuart',count1)
    elif count1<count2:
        print('Kevin',count2)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)