def decodeMorse(morse_code):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-','SOS':'...---...','!':'-.-.--'}
    
    m=morse_code.split('   ')
    l=[]
    n=[]
    for i in range(len(m)):
        l.append(m[i])
    
    for i in l:
        q=i.split()
        n.append(q)
   
    key_l=list(MORSE_CODE_DICT.keys())
    value_l=list(MORSE_CODE_DICT.values())
    a=[]
    b=[]
    for i in range(len(n)):
        for j in range(len(n[i])):
            for k in range(len(value_l)):
                if n[i][j]==value_l[k]:
                    a.append(k)
        a.append(1234) 
                  
    z=[]
    for i in a:
        if i==1234:
            z.append(' ')
        else:
            t=key_l[i]
            z.append(t)
    f=len(z)-1
    del z[f]
    final="".join(z)
    print(final)
decodeMorse('.   .')